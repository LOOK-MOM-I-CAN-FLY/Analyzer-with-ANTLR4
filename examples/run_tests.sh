#!/usr/bin/env bash

set -euo pipefail

TRANSLATOR=${1:-"./build/main"}

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VALID_DIR="$ROOT_DIR/examples/valid"
INVALID_DIR="$ROOT_DIR/examples/invalid"

echo "Транслятор: $TRANSLATOR"
echo "──────────────────────────────────────────"

pass_count=0
fail_count=0

run_case() {
  local expected_ok=$1
  local file=$2

  if $TRANSLATOR "$file" >/dev/null 2>&1; then
    exit_code=0
  else
    exit_code=$?
  fi

  rel_path="${file#$ROOT_DIR/examples/}"

  if [[ "$expected_ok" == "valid" && $exit_code -eq 0 ]]; then
    echo "  PASS  $rel_path"
    pass_count=$((pass_count + 1))
  elif [[ "$expected_ok" == "invalid" && $exit_code -ne 0 ]]; then
    echo "  PASS  $rel_path"
    pass_count=$((pass_count + 1))
  else
    echo "  FAIL  $rel_path (exit code $exit_code)"
    fail_count=$((fail_count + 1))
  fi
}

echo "Положительные примеры (valid/):"
shopt -s nullglob
for f in "$VALID_DIR"/*; do
  run_case "valid" "$f"
done

echo
echo "Негативные примеры (invalid/):"
for f in "$INVALID_DIR"/*; do
  run_case "invalid" "$f"
done

total=$((pass_count + fail_count))
echo
echo "──────────────────────────────────────────"
echo "Итог: $pass_count прошло / $fail_count упало / $total всего"

if [[ $fail_count -ne 0 ]]; then
  exit 1
fi

exit 0
