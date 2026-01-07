document.addEventListener('DOMContentLoaded',function(){
    var messages = document.querySelectorAll(".message");
    messages.forEach(function(message){
        setTimeout(function(){
            message.classList.add('fade-out');
            setTimeout(function(){
                message.remove();
            },500);
        },5000);
        message.querySelector('.close-btn').addEventListener('click',function(){
            message.classList.add('fade-out');
            setTimeout(function(){
                message.remove();
            },500);
        });
    });
});