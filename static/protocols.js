for (let n = 1; n < 32; n++) {
    let now = new Date(2022, 07, n);
    console.log(now)
    if (now.getDay() == 0 || now.getDay() == 6) {
        let element = document.getElementsByClassName(n.toString())
        console.log(element)
        for (var i = 0, max = element.length; i < max; i++) {
            element[i].style.backgroundColor = '#d0d1cf';
        }
    }
}
