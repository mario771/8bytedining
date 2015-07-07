var app = angular.module('myApp', []);

app.controller('RecipeController', function($scope, $http) {
	//needs renaming!
	$http.get('data/data.json').then(function(res) {
		$scope.recipies = res.data;
	});
});

app.controller('CuisineController', function($scope, $http) {
	$http.get('data/cuisines_.json').then(function(res) {
		$scope.cuisines = res.data;
	});
});

app.controller('IngredientController', function($scope, $http) {
	$http.get('data/Ingredients.json').then(function(res) {
		$scope.ingredients = res.data;
	});
});


