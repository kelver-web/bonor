$('body').on("click", ".bi-pencil-square", function() {
    
    $('#marca').val($(this).parents('tr').find('td').eq(0).text());
    $('#modelo').val($(this).parents('tr').find('td').eq(1).text());
    $('#cor').val($(this).parents('tr').find('td').eq(2).text());
    $('#placa').val($(this).parents('tr').find('td').eq(3).text());
    $('#data').val($(this).parents('tr').find('td').eq(4).text());


});

$('body').on("click", ".bi-pencil-square", function(id) {
    
    $('#marca').val($(this).parents('tr').find('td').eq(0).text());
    $('#modelo').val($(this).parents('tr').find('td').eq(1).text());
    $('#cor').val($(this).parents('tr').find('td').eq(2).text());
    $('#placa').val($(this).parents('tr').find('td').eq(3).text());
    $('#data').val($(this).parents('tr').find('td').eq(4).text());


});