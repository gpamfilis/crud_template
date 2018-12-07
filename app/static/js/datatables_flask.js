$(document).ready(function() {
    var this_js_script = $('script[src*=datatables_flask]'); // or better regexp to get the file name..

    var model = this_js_script.attr('model'); 

// example usage
//     <script type="text/javascript">
//     var params = {{ params|safe }};
//     var model = {{model|safe}};
//     console.log(params);
// </script>
// <script src="/static/js/datatables_flask.js"></script>
    // var params = this_js_script.attr('params'); 
    // console.log(params,params.indexOf('token'))

    // console.log('Model Name: ', model)
    // console.log('Form ids: ', params);
    table = $('#example').DataTable({
            "ajax":{

            "url": "/get_data/"+model,
            "dataSrc" :"items"}
    });


// This takes care of the csrftoken situation for flask form submsions.
var csrftoken = $('meta[name=csrf-token]').attr('content')
//console.log(csrftoken);

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$('#example tbody').on( 'click', 'tr', function () {

//console.log('Clicking on row.');

if ( $(this).hasClass('selected') ) {
    //console.log('Unselecting');
    $(this).removeClass('selected');
    $('#add').prop('disabled', false);
    $('#modify').prop('disabled', true);
    $('#delete').prop('disabled', true);
   
    params.forEach(function (value, i) {
        console.log('%d: %s', i, value);
        document.getElementById(value).value = null;
    });
   

    var myURL = document.location.origin;
    console.log(document.location);
    var href = document.location.href;
    var new_url = href.substring(0, href.indexOf('?'));
    window.history.pushState("object or string", "Title", new_url );

}
else {
    // this line unselects the previous one. Find a way to take care of them.
    table.$('tr.selected').removeClass('selected');
    console.log('Selecting');
    $(this).addClass('selected');
    
    // just setting the buttons to the proper state.
    $('#add').prop('disabled', true); 
    $('#modify').prop('disabled', false);
    $('#delete').prop('disabled', false);
    id = table.row('.selected').data()[0];

    var myURL = document.location;
    var origin = myURL.origin;
    var path_name = myURL.pathname;
    console.log(origin,path_name);

    var new_url = origin+path_name + "?project_id="+id;
    window.history.pushState("object or string", "Title", new_url );

    row_data = table.row('.selected').data();
    console.log(row_data);
    
    params.forEach(function (value, i) {
        console.log('%d: %s', i, value);
        document.getElementById(value).value = row_data[i+1];
    });

}
});


$('#delete').click( function () {

    id = table.row('.selected').data()[0];
    console.log(id);
    var choice = window.confirm("Are you sure you want to delete this item?");
    var myURL = document.location.origin;
    var new_url = myURL.substring(0, myURL.indexOf('?'));

    if (choice==true){
        table.row('.selected').remove().draw( false );

        $.ajax({
        type: 'DELETE',
        url: new_url + "/delete_data/"+model+'/'+id,
        data:{"deleting":id},
        success: function(data){
            table.row('.selected').remove().draw( false );
            //document.getElementById("add_item").disabled = false;
            //document.getElementById("edit_item").disabled = true;
            //document.getElementById("delete_row").disabled = true;

        },
        error: function (xhr, statusText, err) {
          alert("error"+xhr.status);
        }
    });}

    else{}


});

// set up update row method without reloading the form.
// set up api/route method for submiting the form
// have tables update it.



} );
