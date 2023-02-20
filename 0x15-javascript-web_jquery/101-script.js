$("document").ready(function () {
  $("DIV#add_item").click(function () {
    //add to the list
    $("UL.my_list").append("<li>Item</li>");
  });
  $("DIV#remove_item").click(function () {
    //remove from the list
    $("UL.my_list li:last").remove();
  });
  $("DIV#clear_list").click(function () {
    //clear the list
    $("UL.my_list").empty();
  });
});
