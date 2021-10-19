// Copyright 2010-2021, Google Inc.
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:
//
//     * Redistributions of source code must retain the above copyright
// notice, this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above
// copyright notice, this list of conditions and the following disclaimer
// in the documentation and/or other materials provided with the
// distribution.
//     * Neither the name of Google Inc. nor the names of its
// contributors may be used to endorse or promote products derived from
// this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#ifndef MOZC_BASE_FILE_UTIL_MOCK_H_
#define MOZC_BASE_FILE_UTIL_MOCK_H_

#include <map>
#include <string>

#include "base/file_util.h"
#include "absl/status/status.h"
#include "absl/strings/str_format.h"

namespace mozc {
class FileUtilMock : public FileUtilInterface {
 public:
  FileUtilMock() { FileUtil::SetMockForUnitTest(this); }
  ~FileUtilMock() override { FileUtil::SetMockForUnitTest(nullptr); }

  // This is not an override function.
  void CreateFile(const std::string &path) {
    files_[path] = base_id_;
    base_id_ += 100'000;
  }

  absl::Status CreateDirectory(const std::string &path) const override {
    if (FileExists(path).ok()) {
      return absl::AlreadyExistsError(path);
    }
    dirs_[path] = true;
    return absl::OkStatus();
  }

  absl::Status RemoveDirectory(const std::string &dirname) const override {
    if (FileExists(dirname).ok()) {
      return absl::NotFoundError(dirname);
    }
    dirs_[dirname] = false;
    return absl::OkStatus();
  }

  absl::Status Unlink(const std::string &filename) const override {
    if (DirectoryExists(filename).ok()) {
      return absl::FailedPreconditionError(
          absl::StrFormat("%s is a directory", filename));
    }
    files_[filename] = 0;
    return absl::OkStatus();
  }

  absl::Status FileExists(const std::string &filename) const override {
    const auto it = files_.find(filename);
    return it != files_.end() && it->second > 0 ? absl::OkStatus()
                                                : absl::NotFoundError(filename);
  }

  absl::Status DirectoryExists(const std::string &dirname) const override {
    auto it = dirs_.find(dirname);
    return it != dirs_.end() && it->second ? absl::OkStatus()
                                           : absl::NotFoundError(dirname);
  }

  absl::Status CopyFile(const std::string &from,
                        const std::string &to) const override {
    if (!FileExists(from).ok()) {
      return absl::NotFoundError(from);
    }
    files_[to] = files_[from];
    return absl::OkStatus();
  }

  bool IsEqualFile(const std::string &filename1,
                   const std::string &filename2) const override {
    return (FileExists(filename1).ok() && FileExists(filename2).ok() &&
            files_[filename1] == files_[filename2]);
  }

  bool IsEquivalent(const std::string &filename1,
                    const std::string &filename2) const override {
    const std::string canonical1 = At(canonical_paths_, filename1, filename1);
    const std::string canonical2 = At(canonical_paths_, filename2, filename2);
    return canonical1 == canonical2;
  }

  absl::Status AtomicRename(const std::string &from,
                            const std::string &to) const override {
    if (FileExists(from).ok()) {
      files_[to] = files_[from];
      files_[from] = 0;
      return absl::OkStatus();
    }
    if (DirectoryExists(from).ok()) {
      dirs_[to] = dirs_[from];
      dirs_[from] = false;
      return absl::OkStatus();
    }
    return absl::NotFoundError(absl::StrFormat("%s doesn't exist", from));
  }

  bool CreateHardLink(const std::string &from, const std::string &to) override {
    if (!FileExists(from).ok() && !DirectoryExists(from).ok()) {
      // `from` doesn't exist.
      return false;
    }

    if (FileExists(to).ok() || DirectoryExists(to).ok()) {
      // `to` already exists.
      return false;
    }

    canonical_paths_[to] = from;
    if (FileExists(from).ok()) {
      CreateFile(to);
      return true;
    }
    return CreateDirectory(to).ok();
  }

  bool GetModificationTime(const std::string &filename,
                           FileTimeStamp *modified_at) const override {
    if (!FileExists(filename).ok()) {
      return false;
    }
    *modified_at = files_[filename];
    return true;
  }

  // Use FileTimeStamp as time stamp and also file id.
  // 0 means that the file is removed.
  mutable std::map<std::string, FileTimeStamp> files_;
  FileTimeStamp base_id_{1'000'000'000};
  mutable std::map<std::string, bool> dirs_;
  mutable std::map<std::string, std::string> canonical_paths_;

 private:
  template <typename T>
  T At(const std::map<std::string, T> &map, const std::string &key,
       const T &fallback_value) const {
    auto it = map.find(key);
    return it == map.end() ? fallback_value : it->second;
  }
};
}  // namespace mozc

#endif  // MOZC_BASE_FILE_UTIL_MOCK_H_
