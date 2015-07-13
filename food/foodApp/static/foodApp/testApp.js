var app = angular.module('testApp', []);

app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('[[');
	$interpolateProvider.endSymbol(']]');
});

app.controller("TestController", function($scope) {

	$scope.test = "hello";

});

app.controller("LocationController", function($scope, $location) {
/*
	$scope.$location = {};
	angular.forEach("protocol host port path search hash".split(" "), function(method){
		$scope.$location[method] = function(){
			var result = $location[method].call($location);
			return angular.isObject(result) ? angular.toJson(result) : result;
		};
	});
*/


	$scope.absUrl = $location.absUrl();
	//$scope.url = $location.url();

	$scope.test = "working";
});