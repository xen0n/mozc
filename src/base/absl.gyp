# Copyright 2010-2021, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'conditions': [
    ['use_system_abseil_cpp==0', {
      'variables': {
        'absl_srcdir': '<(DEPTH)/third_party/abseil-cpp/absl',
        'gen_absl_dir': '<(SHARED_INTERMEDIATE_DIR)/third_party/abseil-cpp/absl',
      },
    }],
  ],
  'targets': [
    {
      'target_name': 'absl_base',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_base -labsl_city -labsl_hash -labsl_malloc_internal -labsl_raw_hash_set -labsl_raw_logging_internal -labsl_spinlock_wait -labsl_status -labsl_strings -labsl_strings_internal -labsl_throw_delegate -labsl_debugging_internal -labsl_synchronization -labsl_time',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_base -labsl_base
            '<(absl_srcdir)/base/internal/cycleclock.cc',
            # libabsl_malloc_internal -labsl_malloc_internal
            '<(absl_srcdir)/base/internal/low_level_alloc.cc',
            # libabsl_raw_logging_internal -labsl_raw_logging_internal
            '<(absl_srcdir)/base/internal/raw_logging.cc',
            # libabsl_base -labsl_base
            '<(absl_srcdir)/base/internal/spinlock.cc',
            # libabsl_spinlock_wait -labsl_spinlock_wait
            '<(absl_srcdir)/base/internal/spinlock_wait.cc',
            # libabsl_base -labsl_base
            '<(absl_srcdir)/base/internal/sysinfo.cc',
            '<(absl_srcdir)/base/internal/thread_identity.cc',
            # libabsl_throw_delegate -labsl_throw_delegate
            '<(absl_srcdir)/base/internal/throw_delegate.cc',
            # libabsl_base -labsl_base
            '<(absl_srcdir)/base/internal/unscaledcycleclock.cc',
            # libabsl_log_severity.so -labsl_log_severity
            '<(absl_srcdir)/base/log_severity.cc',
            # libabsl_exponential_biased -labsl_exponential_biased
            '<(absl_srcdir)/profiling/internal/exponential_biased.cc',
          ],
          'dependencies': [
            'absl_hash_internal',
          ],
          'msvs_disabled_warnings': [
            # 'type' : forcing value to bool 'true' or 'false'
            # (performance warning)
            # http://msdn.microsoft.com/en-us/library/b6801kcy.aspx
            '4800',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_debugging',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_stacktrace -labsl_symbolize -labsl_debugging_internal -labsl_debug -labsl_synchronization',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_stacktrace -labsl_stacktrace
            '<(absl_srcdir)/debugging/stacktrace.cc',
            # libabsl_symbolize -labsl_symbolize
            '<(absl_srcdir)/debugging/symbolize.cc',
            # libabsl_debugging_internal -labsl_debugging_internal
            '<(absl_srcdir)/debugging/internal/address_is_readable.cc',
            '<(absl_srcdir)/debugging/internal/demangle.cc',
            '<(absl_srcdir)/debugging/internal/elf_mem_image.cc',
            '<(absl_srcdir)/debugging/internal/vdso_support.cc',
          ],
          'dependencies': [
            'absl_base',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_flags',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_flags_internal -labsl_raw_hash_set -labsl_city -labsl_hash -labsl_low_level_hash -labsl_synchronization -labsl_flags_reflection -labsl_flags_marshalling',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_flags_commandlineflag -labsl_flags_commandlineflag
            '<(absl_srcdir)/flags/commandlineflag.cc',
            '<(absl_srcdir)/flags/commandlineflag.h',
            # libabsl_flags_usage -labsl_flags_usage
            '<(absl_srcdir)/flags/usage.cc',
            '<(absl_srcdir)/flags/usage.h',
            # libabsl_flags -labsl_flags -labsl_flags_internal
            '<(absl_srcdir)/flags/flag.cc',
            '<(absl_srcdir)/flags/flag.h',
            # libabsl_flags_config -labsl_flags_config
            '<(absl_srcdir)/flags/config.h',
            # libabsl_flags -labsl_flags
            '<(absl_srcdir)/flags/declare.h',
            # libabsl_flags_marshalling -labsl_flags_marshalling
            '<(absl_srcdir)/flags/marshalling.cc',
            '<(absl_srcdir)/flags/marshalling.h',
            # libabsl_flags_parse -labsl_flags_parse
            '<(absl_srcdir)/flags/parse.cc',
            '<(absl_srcdir)/flags/parse.h',
            # libabsl_flags_reflection -labsl_flags_reflection
            '<(absl_srcdir)/flags/reflection.cc',
            '<(absl_srcdir)/flags/reflection.h',
            # libabsl_flags -labsl_flags
            '<(absl_srcdir)/flags/usage_config.cc',
            '<(absl_srcdir)/flags/usage_config.h',
          ],
          'dependencies': [
            'absl_flags_internal',
            'absl_hash_internal',
            'absl_synchronization',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_flags_internal',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_flags_commandlineflag_internal -labsl_flags_usage -labsl_flags_usage_internal -labsl_flags_internal -labsl_flags_private_handle_accessor -labsl_flags_program_name -labsl_flags_parse',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_flags_commandlineflag_internal -labsl_flags_commandlineflag_internal
            '<(absl_srcdir)/flags/internal/commandlineflag.cc',
            '<(absl_srcdir)/flags/internal/commandlineflag.h',
            # libabsl_flags_internal -labsl_flags_internal
            '<(absl_srcdir)/flags/internal/flag.cc',
            '<(absl_srcdir)/flags/internal/flag.h',
            # libabsl_flags_parse -labsl_flags_parse
            '<(absl_srcdir)/flags/internal/parse.h',
            # libabsl_flags_internal -labsl_flags_internal
            '<(absl_srcdir)/flags/internal/path_util.h',
            # libabsl_flags_private_handle_accessor -labsl_flags_private_handle_accessor
            '<(absl_srcdir)/flags/internal/private_handle_accessor.cc',
            '<(absl_srcdir)/flags/internal/private_handle_accessor.h',
            # libabsl_flags_program_name -labsl_flags_program_name
            '<(absl_srcdir)/flags/internal/program_name.cc',
            '<(absl_srcdir)/flags/internal/program_name.h',
            # libabsl_flags_internal -labsl_flags_internal
            '<(absl_srcdir)/flags/internal/registry.h',
            # libabsl_flags_usage_internal -labsl_flags_usage_internal libabsl_flags_usage -labsl_flags_usage
            '<(absl_srcdir)/flags/internal/usage.cc',
            '<(absl_srcdir)/flags/internal/usage.h',
          ],
          'dependencies': [
            'absl_strings',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_hash_internal',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_raw_hash_set -labsl_city -labsl_hash -labsl_low_level_hash',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_raw_hash_set -labsl_raw_hash_set
            '<(absl_srcdir)/container/internal/raw_hash_set.cc',
            # libabsl_city -labsl_city
            '<(absl_srcdir)/hash/internal/city.cc',
            # libabsl_hash -labsl_hash
            '<(absl_srcdir)/hash/internal/hash.cc',
            # libabsl_low_level_hash -labsl_low_level_hash
            '<(absl_srcdir)/hash/internal/low_level_hash.cc',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_numeric',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_int128',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_int128 -labsl_int128
            '<(absl_srcdir)/numeric/int128.cc',
          ],
          'dependencies': [
            'absl_base',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_random',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_random_distributions -labsl_random_internal_pool_urbg -labsl_random_internal_randen -labsl_random_internal_randen_hwaes -labsl_random_internal_randen_hwaes_impl -labsl_random_internal_randen_slow -labsl_random_internal_seed_material -labsl_random_seed_gen_exception -labsl_random_seed_sequences',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
        #'<(absl_srcdir)/random/discrete_distribution.cc',
        #'<(absl_srcdir)/random/gaussian_distribution.cc',
        '<(absl_srcdir)/random/internal/chi_square.cc',
        #'<(absl_srcdir)/random/internal/pool_urbg.cc',
        #'<(absl_srcdir)/random/internal/randen.cc',
        '<(absl_srcdir)/random/internal/randen_detect.cc',
        #'<(absl_srcdir)/random/internal/randen_hwaes.cc',
        '<(absl_srcdir)/random/internal/randen_round_keys.cc',
        #'<(absl_srcdir)/random/internal/randen_slow.cc',
        #'<(absl_srcdir)/random/internal/seed_material.cc',
        #'<(absl_srcdir)/random/seed_gen_exception.cc',
        #'<(absl_srcdir)/random/seed_sequences.cc',
          ],
          'dependencies': [
            'absl_base',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_strings_internal',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_strings_internal -labsl_strings -labsl_time -labsl_cord_internal -labsl_cordz_functions -labsl_cordz_handle -labsl_cordz_info -labsl_str_format_internal',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_strings_internal -labsl_strings_internal
            '<(absl_srcdir)/strings/internal/charconv_bigint.cc',
            '<(absl_srcdir)/strings/internal/charconv_parse.cc',
            # libabsl_cord_internal -labsl_cord_internal
            '<(absl_srcdir)/strings/internal/cord_internal.cc',
            '<(absl_srcdir)/strings/internal/cord_rep_btree.cc',
            '<(absl_srcdir)/strings/internal/cord_rep_btree_navigator.cc',
            '<(absl_srcdir)/strings/internal/cord_rep_btree_reader.cc',
            '<(absl_srcdir)/strings/internal/cord_rep_consume.cc',
            '<(absl_srcdir)/strings/internal/cord_rep_ring.cc',
            # libabsl_cordz_functions -labsl_cordz_functions
            '<(absl_srcdir)/strings/internal/cordz_functions.cc',
            # libabsl_cordz_handle -labsl_cordz_handle
            '<(absl_srcdir)/strings/internal/cordz_handle.cc',
            # libabsl_cordz_info -labsl_cordz_info
            '<(absl_srcdir)/strings/internal/cordz_info.cc',
            # libabsl_strings_internal -labsl_strings_internal
            '<(absl_srcdir)/strings/internal/escaping.cc',
            '<(absl_srcdir)/strings/internal/memutil.cc',
            # libabsl_str_format_internal -labsl_str_format_internal
            '<(absl_srcdir)/strings/internal/str_format/arg.cc',
            '<(absl_srcdir)/strings/internal/str_format/bind.cc',
            '<(absl_srcdir)/strings/internal/str_format/extension.cc',
            '<(absl_srcdir)/strings/internal/str_format/float_conversion.cc',
            '<(absl_srcdir)/strings/internal/str_format/output.cc',
            '<(absl_srcdir)/strings/internal/str_format/parser.cc',
            '<(absl_srcdir)/strings/internal/utf8.cc',
          ],
          'dependencies': [
            'absl_base',
            'absl_numeric',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_strings',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_str_format_internal -labsl_strings -labsl_strings_internal -labsl_flags_internal -labsl_status',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_strings -labsl_strings
            '<(absl_srcdir)/strings/ascii.cc',
            '<(absl_srcdir)/strings/charconv.cc',
            '<(absl_srcdir)/strings/cord.cc',
            '<(absl_srcdir)/strings/escaping.cc',
            '<(absl_srcdir)/strings/match.cc',
            '<(absl_srcdir)/strings/numbers.cc',
            '<(absl_srcdir)/strings/str_cat.cc',
            '<(absl_srcdir)/strings/str_replace.cc',
            '<(absl_srcdir)/strings/str_split.cc',
            '<(absl_srcdir)/strings/string_view.cc',
            '<(absl_srcdir)/strings/substitute.cc',
          ],
          'dependencies': [
            'absl_base',
            'absl_numeric',
            'absl_strings_internal',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_synchronization',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_synchronization -labsl_graphcycles_internal -labsl_string_view',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_synchronization -labsl_synchronization
            '<(absl_srcdir)/synchronization/barrier.cc',
            '<(absl_srcdir)/synchronization/blocking_counter.cc',
            '<(absl_srcdir)/synchronization/blocking_counter.cc',
            '<(absl_srcdir)/synchronization/internal/create_thread_identity.cc',
            '<(absl_srcdir)/synchronization/internal/create_thread_identity.cc',
            # libabsl_graphcycles_internal -labsl_graphcycles_internal
            '<(absl_srcdir)/synchronization/internal/graphcycles.cc',
            '<(absl_srcdir)/synchronization/internal/graphcycles.cc',
            # libabsl_synchronization -labsl_synchronization
            '<(absl_srcdir)/synchronization/internal/per_thread_sem.cc',
            '<(absl_srcdir)/synchronization/internal/waiter.cc',
            '<(absl_srcdir)/synchronization/mutex.cc',
          ],
          'dependencies': [
            'absl_base',
            'absl_debugging',
            'absl_time',
            'absl_numeric',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_time',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_civil_time -labsl_synchronization -labsl_time -labsl_time_zone',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_civil_time -labsl_civil_time
            '<(absl_srcdir)/time/civil_time.cc',
            # libabsl_time -labsl_time
            '<(absl_srcdir)/time/clock.cc',
            '<(absl_srcdir)/time/duration.cc',
            '<(absl_srcdir)/time/format.cc',
            '<(absl_srcdir)/time/time.cc',
            # libabsl_time_zone -labsl_time_zone
            '<(absl_srcdir)/time/internal/cctz/src/civil_time_detail.cc',
            '<(absl_srcdir)/time/internal/cctz/src/time_zone_fixed.cc',
            '<(absl_srcdir)/time/internal/cctz/src/time_zone_format.cc',
            '<(absl_srcdir)/time/internal/cctz/src/time_zone_if.cc',
            '<(absl_srcdir)/time/internal/cctz/src/time_zone_impl.cc',
            '<(absl_srcdir)/time/internal/cctz/src/time_zone_info.cc',
            '<(absl_srcdir)/time/internal/cctz/src/time_zone_libc.cc',
            '<(absl_srcdir)/time/internal/cctz/src/time_zone_lookup.cc',
            '<(absl_srcdir)/time/internal/cctz/src/time_zone_posix.cc',
            '<(absl_srcdir)/time/internal/cctz/src/zone_info_source.cc',
          ],
          'cflags': [
            '-Wno-error',
          ],
          'dependencies': [
            'absl_base',
            'absl_numeric',
            'absl_strings_internal',
          ],
        }],
      ],
    },
    {
      'target_name': 'absl_status',
      'toolsets': ['host', 'target'],
      'conditions': [
        ['use_system_abseil_cpp==1', {
          'type': 'none',
          'all_dependent_settings': {
            'link_settings': {
              'libraries': [
                '-labsl_status -labsl_statusor',
              ],
            },
          },
        }, {
          'type': 'static_library',
          'sources': [
            # libabsl_status -labsl_status
            '<(absl_srcdir)/status/status.cc',
            '<(absl_srcdir)/status/status_payload_printer.cc',
            # libabsl_statusor -labsl_statusor
            '<(absl_srcdir)/status/statusor.cc',
          ],
          'dependencies': [
            'absl_base',
            'absl_strings',
          ],
        }],
      ],
    },
  ],
}
