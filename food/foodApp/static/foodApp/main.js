var app = angular.module('myApp', [],function($locationProvider) {
	$locationProvider.html5Mode(true);
});

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});

app.controller('RecipeController', function($scope, $http, $location) {
	$scope.recipe = $location.search()["r"];

	$http.get('/static/foodApp/RecipeData.json').then(function(res) {
		$scope.recipes = res.data;
	});
});
/*
app.controller('CuisineController', function($scope, $http) {
	//EMPTY
	$http.get('/static/foodApp/cuisines_.json').then(function(res) {
		$scope.cuisines = res.data;
	});
});

app.controller('IngredientController', function($scope, $http) {
	//EMPTY
	$http.get('/static/foodApp/Ingredients.json').then(function(res) {
		$scope.ingredients = res.data;
	});
});
*/



