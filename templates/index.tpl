<!DOCTYPE html>
<html>
<head>
    <title>Music Downloader</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/bootstrap.css') }}">

</head>
<body>
    <div class="container">
        <h1>Music Downloader</h1>
        <div class="form-horizontal">
            <div class="form-group">
                <label for="inputSearch" class="col-sm-2 control-label">Search Term</label>
                <div class="col-sm-8">
                    <input type="text" class="form-control" id="inputSearch" placeholder="Song Name / Lyrics / Artist">
                </div>
            </div>
        </div>
        <div class="col-sm-offset-2">
            <div class="btn btn-primary" id="btnSearch">
                <span class="glyphicon glyphicon-search"></span>
                &nbsp;Search
            </div>
        </div>
    </div>
    <script type="text/javascript" src="{{ url_for('static', filename='js/jquery-2.1.4.min.js') }}"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='js/jquery.noty.packaged.js') }}"></script>
    <script type="text/javascript">
    function confirmation(text, link){
        var n = noty({
            text        : 'Do you want to download '+text+'?',
            type        : 'information',
            dismissQueue: true,
            layout      : 'center',
            theme       : 'defaultTheme',
            buttons     : [
                {addClass: 'btn btn-primary', text: 'Ok', onClick: function ($noty) {
                $noty.close();
                    console.log('Downloading '+link);
                    location.href = '/song_download?video_link='+encodeURIComponent(link)+'&title='+encodeURIComponent(text);
                    }
                },
            {addClass: 'btn btn-danger', text: 'Cancel', onClick: function ($noty) {
                $noty.close();
                }
            }
            ]});
            console.log('html: ' + n.options.id);
        }
    $(function(){
        $('#btnSearch').click(function(){
            var searchString = encodeURIComponent($('#inputSearch').val());
            $.ajax({
                url: '/ajax/search?search_string='+searchString,
                cache: false
            }).done(function( result ) {
                var array = JSON.parse(result);
                console.log(array);
                confirmation(array.title, array.video_link);
            });
        });
        $(document).keypress(function(e){
            if (e.which == 13){
                $('#btnSearch').click();
            }
        });
    });
    </script>
</body>
</html>
