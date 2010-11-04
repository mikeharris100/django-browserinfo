var browserinfo = {
    
    jQuery : $,
    
    harvest : function (url, settings) {
        var contacts    =   this,
        $               =   this.jQuery;

        settings = $.extend({
            callback: false,
        }, settings);

        var d = new Date();
        var loc = d.toLocaleString();
        var tz = loc.substr(loc.indexOf('(')+1, 3);

        var vars = {
            'colour_depth' : screen.colorDepth,
            'screen_height' : screen.height,
            'screen_width' : screen.width,
            'browser_height' : window.innerHeight,
            'browser_width' : window.innerWidth,
            'timezone' : tz,
        };

        $.ajax({
            url: url,
            type: 'POST',
            async: true,
            data: vars,
            dataType: 'json',
            traditional: true,
            error: function(XHR, textStatus, errorThrown){
                console.log(textStatus);
            },
            success: settings.callback 
        });
    }
};

