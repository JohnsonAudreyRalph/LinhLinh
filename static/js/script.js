// $(document).ready(function(){
//     const showHiddenPass = (loginPass, loginEye) => {
//         const input = document.getElementById(loginPass),
//         iconEye = document.getElementById(loginEye);
      
//         iconEye.addEventListener('click', () => {
//             if (input.type === 'password') {
//                 input.type = 'text';
                
//                 iconEye.classList.add('ri-eye-line');
//                 iconEye.classList.remove('ri-eye-off-line');
//             }
//             else {
//                 input.type = 'password';
//                 iconEye.classList.remove('ri-eye-line');
//                 iconEye.classList.add('ri-eye-off-line');
//             }
//         });
//     };

//     showHiddenPass('login-pass', 'login-eye');
// });


// $(document).ready(function() {
//     $(window).scroll(function() {
//         if($(this).scrollTop()) {
//            $('#backtop').fadeIn(); 
//         } else{
//             $('#backtop').fadeOut();
//         }
//     });
//     $("#backtop").click(function() {
//         $('html, body').animate({
//             scrollTop: 0
//         }, 500);
//     });
// }); 


// let fall = document.getElementById('fall');
// let count = 50;
// for(var d = 0; d<50; d++){
//     let leftSnow = Math.floor(Math.random() * fall.clientWidth);
//     let topSnow = Math.floor(Math.random() * fall.clientHeight);
//     let widthSnow = Math.floor(Math.random() * 50);
//     let timeSnow = Math.floor((Math.random() * 5) + 5);
//     let blurSnow = Math.floor(Math.random() * 5);
//     console.log(leftSnow);
//     let div = document.createElement('div');
//     div.classList.add('snow');
//     div.style.left = leftSnow + 'px';
//     div.style.top = topSnow + 'px';
//     div.style.width = widthSnow + 'px';
//     div.style.height = widthSnow + 'px';
//     div.style.animationDuration = timeSnow + 's';
//     div.style.filter = "blur(" + blurSnow + "px)";
//     fall.appendChild(div);
// }
// alert('xxx')