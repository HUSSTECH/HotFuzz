//Data Class
function ministry(data) {
    this.name = ko.observable(data);
}

var ViewModel = function() {

    var self = this;
    self.query = ko.observable("");
    self.ministries = ko.observableArray([]);
    self.URI = './outputList'

    $.getJSON(self.URI,
        {querystring:self.query},
        function(data) {
            var mappeditems = $.map(data.ministries, function(item){return new ministry(item)});
            self.ministries(mappeditems);
        });

    self.update = function() {
        $.getJSON(self.URI,
            {querystring:self.query},
            function(data) {
                var mappeditems = $.map(data.ministries, function(item){return new ministry(item)});
                self.ministries(mappeditems);
            });        
        return true;
    }
    
};
 
ko.applyBindings(new ViewModel());
