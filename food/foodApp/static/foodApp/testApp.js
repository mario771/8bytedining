var app = angular.module('testApp', [],function($locationProvider) {
	$locationProvider.html5Mode(true);
});

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});

app.controller("TestController", function($scope, $location, $http) {
	$scope.url = $location.absUrl();
	$scope.ohboy = $location.search();
	$scope.recipe = $location.search()["r"];
	$scope.hello = "functioning";
	$scope.fj = {"auntruthiespotroast" : "you did it!!"};

	$http.get('/static/foodApp/RecipeData.json').then(function(res) {
		$scope.recipes = res.data;
	});
});
