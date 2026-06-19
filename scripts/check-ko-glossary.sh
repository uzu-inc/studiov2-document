#!/usr/bin/env sh
set -eu

target_dir="${1:-packages/ko}"

if [ ! -d "$target_dir" ]; then
  echo "Target directory not found: $target_dir" >&2
  exit 2
fi

status=0

check_term() {
  bad="$1"
  good="$2"
  if rg -n --glob '*.md' "$bad" "$target_dir"; then
    echo
    echo "Use '$good' instead of '$bad'."
    echo
    status=1
  fi
}

check_term '우즈스튜디오' '우즈 스튜디오'
check_term '마더 미스터리' '머더 미스터리'
check_term '행동 실행' '액션 실행'
check_term '결과 행동' '결과 액션'
check_term '페이즈' '단계'
check_term '덱' '더미'
check_term '레포트' '리포트'
check_term '나레이션' '내레이션'
check_term '출시' '릴리스'
check_term '양식' '폼'
check_term '반복 플레이 캐릭터' '특수 캐릭터 유형'
check_term '자유 입력' '자유 기재'
check_term '자유 서술' '자유 기재'
check_term '자유 기입' '자유 기재'
check_term '테이블' '방'
check_term '감상전 화면' '감상 공유 화면'
check_term '열람권' '열람 권한'

exit "$status"
