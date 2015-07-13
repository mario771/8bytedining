var app = angular.module('testApp', []);

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});

app.controller("TestController", function($scope) {

	$scope.test = "hello";

});

/*
app.controller("LocationController", function($scope, $location, $http) {
	$scope.$location = {};
	angular.forEach("protocol host port path search hash".split(" "), function(method){
		$scope.$location[method] = function(){
			var result = $location[method].call($location);
			return angular.toJson(result);
			//return angular.isObject(result) ? angular.toJson(result) : result;
		};
	});

	$http.get('data/info.json').then(function(res) {
		$scope.blah = res.data;
	});

	$scope.url = $location.url();

	$scope.test = "working";
	
	//$location.url().then(function(res2) {
	//	$scope.test = res2;
	//});
});
*/
