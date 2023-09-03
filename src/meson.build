python = import('python')

# ===== Generate Calculator bin ===== 
configure_file(
  input: 'calculator.in',
  output: 'calculator',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
)

# ===== Generate define module
configure_file(
  input: 'define.in',
  output: 'define.py',
  configuration: conf,
  install: true,
  install_dir: moduledir
)

launcher = join_paths(meson.project_build_root(), 'src', meson.project_name())
run_target('run',
  command: [launcher]
)

# ===== Blueprint compiler =====
blueprints = custom_target('blueprints',
  input: files(
    'components/shortcuts/shortcuts.blp',
    'components/theme_selector/theme_selector.blp',
    'window.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

# ===== Compile Calculator gresource =====
gnome.compile_resources('calculator',
  'calculator.gresource.xml',
  dependencies: blueprints,
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

# ===== Python sources =====
sources = [
  '__init__.py',
  'components/theme_selector/theme_selector.py',
  'components/shortcuts/shortcuts.py',
  'main.py',
  'window.py',
]

# ===== Install python sources =====
install_data(sources, install_dir: moduledir)

# ===== Install components sources =====
install_subdir('components', install_dir: moduledir)

# ===== Install assets sources =====
install_subdir('assets', install_dir: moduledir)
