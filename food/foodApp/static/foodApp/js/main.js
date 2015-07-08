var app = angular.module('myApp', []);

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
});

app.controller('RecipeController', function($scope, $http) {
	//needs renaming!
	$http.get('/static/foodApp/data/data.json').then(function(res) {
		$scope.recipies = res.data;
	});
	$http.get('/static/foodApp/data/Recipe_tables.json').then(function(res) {
		$scope.rmodels = res.data;
	});
});

app.controller('CuisineController', function($scope, $http) {
	$http.get('/static/foodApp/data/cuisines_.json').then(function(res) {
		$scope.cuisines = res.data;
	});
	$http.get('/static/foodApp/data/Cuisine_tables.json').then(function(res) {
		$scope.cmodels = res.data;
	});
});

app.controller('IngredientController', function($scope, $http) {
	$http.get('/static/foodApp/data/Ingredients_.json').then(function(res) {
		$scope.ingredients = res.data;
	});
	$http.get('/static/foodApp/data/Ingredients_table.json').then(function(res) {
		$scope.imodels = res.data;
	});
});


