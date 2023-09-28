console.log("inside functions")

var li_components = document.getElementsByClassName("nav-link")

console.log(li_components)


window.onload = function () {
  for (let i = 0; i < li_components.length; i++) {
    li_components[i].addEventListener("click", function(e){
      for (let i = 0; i < li_components.length; i++) {
         li_components[i].classList.remove('active');
         e.target.classList.add('active');
      };
      console.log(e.target.classList);
    })
  }
}