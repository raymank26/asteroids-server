var app = angular.module("asteroids", []);

app.controller('score', ['$http', '$scope', function($http, $scope){
    $scope.scores = [];
    $http.get("/scores/top10/").success(function (scores) {
        $scope.scores = scores;
    });
}]);
