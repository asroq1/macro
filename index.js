window.onload = function () {
  // 관찰할 요소를 찾습니다.
  const targetElement = document.querySelector(
    '.choose-areas-results__body--results__items--item'
  )

  if (targetElement) {
    // Intersection Observer를 생성합니다.
    const observer = new IntersectionObserver(
      (entries, observer) => {
        // 콜백 함수입니다.
        alert('콜백 함수가 실행되었습니다.')
        entries.forEach(entry => {
          // 버튼이 화면에 나타났는지 확인합니다.
          if (
            entry.target.classList.contains(
              'choose-areas-results__body--results__items--item'
            )
          ) {
            // 클래스 요소를 찾습니다.
            const element = document.querySelector(
              '.choose-areas-results__body--results__items--item'
            )

            // 클래스 요소가 존재하는지 확인합니다.
            if (element) {
              // 요소가 존재하면 원하는 작업을 수행합니다.
              console.log('요소가 존재합니다.')
            } else {
              // 요소가 존재하지 않으면 원하는 작업을 수행합니다.
              console.log('요소가 존재하지 않습니다.')
            }
          }
        })
      },
      {
        // 특정 클래스를 가진 버튼만 관찰
        root: null,
        rootMargin: '0px',
        threshold: 0.0,
      }
    )

    // 관찰을 시작합니다.
    if (targetElement) {
      observer.observe(targetElement)
    } else {
      console.log('관찰할 요소가 존재하지 않습니다.')
    }
  } else {
    console.log('관찰할 요소가 존재하지 않습니다.')
  }
}
