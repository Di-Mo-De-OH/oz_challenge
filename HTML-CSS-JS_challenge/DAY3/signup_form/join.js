const form = document.querySelector("#form");

form.addEventListener("submit",function(event){
    event.preventDefault()

    let userId = event.target.id.value;
    let userPassword = event.target.password.value;
    let userPassword1 = event.target.password1.value;
    let userName = event.target.name.value;
    let userPhone = event.target.phone.value;
    let userPosition = event.target.position.value;
    let useGender = event.target.gender.value;
    let userEmail = event.target.email.value;
    let userIntro = event.target.intro.value;


    if(userId.length<6){
        alert("아이디가 너무 짧습니다.6자 이상 입력해주세요.")
        return 
    }

    if(userPassword !== userPassword1){
        alert("비밀번호가 일치하지 않습니다.")
        return 
    }

    // 가입 잘 되었다! 환영!
    document.body.innerHTML = ""
    document.write(`<p>${userId}님 환영합니다</p>`)



})