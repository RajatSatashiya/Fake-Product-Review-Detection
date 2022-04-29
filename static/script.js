var revname = document.querySelector(".revname");
var revdesc = document.querySelector(".revdesc");
var theform = document.forms["thename"];

const addReview = () => {
  revname.innerHTML = "- " + theform.elements["name"].value;
  revdesc.innerHTML = theform.elements["review"].value;
};
