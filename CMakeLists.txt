cmake_minimum_required(VERSION 3.15)

project(MyLanguagePython NONE)

# CMake здесь используется только как «сборочная система»,
# которая создаёт исполняемый скрипт ./build/main,
# полностью совместимый с требованиями:
#   ./build/main examples/valid/...

set(MAIN_SCRIPT "${CMAKE_BINARY_DIR}/main")
set(VENV_PYTHON "${CMAKE_SOURCE_DIR}/.venv/bin/python")

if(EXISTS "${VENV_PYTHON}")
  set(PYTHON_EXECUTABLE "${VENV_PYTHON}")
else()
  find_program(PYTHON_EXECUTABLE python3)
endif()

file(WRITE "${MAIN_SCRIPT}" "#!/usr/bin/env bash\n")
file(APPEND "${MAIN_SCRIPT}" "\"${PYTHON_EXECUTABLE}\" -m src.main \"$@\"\n")

file(CHMOD "${MAIN_SCRIPT}"
  PERMISSIONS
    OWNER_READ OWNER_WRITE OWNER_EXECUTE
    GROUP_READ GROUP_EXECUTE
    WORLD_READ WORLD_EXECUTE
)

add_custom_target(main ALL DEPENDS "${MAIN_SCRIPT}")
