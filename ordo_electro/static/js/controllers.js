/**
 * INSPINIA - Responsive Admin Theme
 * Copyright 2015 Webapplayers.com
 *
 */

/**
 * MainCtrl - controller
 */
function MainCtrl() {

    this.userName = 'Example user';
    this.helloText = 'Welcome in SeedProject';
    this.descriptionText = 'It is an application skeleton for a typical AngularJS web app. You can use it to quickly bootstrap your angular webapp projects and dev environment for these projects.';

};

/**
 * SocialAccountsCtrl - Social User Accounts 
 * used all over the place probably 
 * sets the dominant account for a screen 
 */
function SocialAccountsCtrl($scope, $http) {
	
	$scope.socialAccounts = [];
	$scope.activeAccount = null;
	
	// activeSocialAccount --- stores the holder 
	$http({
		method : 'GET',
		url : '/social/accounts/'
	}).success(function(result) {
		$scope.socialAccounts = result;
	});
	
}

/**
 * Twitter account stuff 
 * sets the dominant account for a screen 
 */
function TwitterAccountsCtrl($scope, $http) {
	
	$scope.twitterAccounts = [];
	
	// activeSocialAccount --- stores the holder 
	$http({
		method : 'GET',
		url : '/social/twitter/accounts/'
	}).success(function(result) {
		$scope.twitterAccounts = result;
	});

}

// For now I'll stuff this in here until I can get best practices
// Define CreditCard class

//var TwitterAccount = $resource('/social/twitter/accounts/:id', {id:'@id'});


//var TwitterAccount = function($resource) {
//	$resource('/social/twitter/accounts/:id', {
//		twitter_id : '@id'
//	}, {
//		update : {
//			method : 'PUT'
//		}
//	})
//};

function TwitterAccountsCtrlX($scope, TwitterAccount) {

	$scope.twitterAccount = TwitterAccount.get({id: $scope.id }); // get() returns a single entry

	$scope.twitterAccounts = TwitterAccount.query(); // query() returns all the entries
//
//	$scope.twitterAccount = new twitterAccount(); // You can instantiate resource class
//
//	$scope.twitterAccount.data = 'TBD';
//
//	TwitterAccount.save($scope.entry, function() {
//		// data saved. do something here.
//	}); // saves an entry. Assuming $scope.entry is the Entry object

	// // list of accounts assoicated to this users
	// $http({
	// method : 'GET',
	// url : '/social/twitter/accounts/'
	// }).success(function(result) {
	// $scope.socialAccount = result;
	// });
}
var TwitterAccount = function ($resource) {
	return $resource('/social/twitter/accounts/:id',
			{id:'@id'},
    		{'query': { method: 'GET', isArray:true }}
    		);
}

angular
    .module('inspinia')
    .controller('MainCtrl', MainCtrl)
    .controller('SocialAccountsCtrl', SocialAccountsCtrl)
    .controller('TwitterAccountsCtrl', TwitterAccountsCtrl)
    .factory('TwitterAccount',TwitterAccount)
   
//ta = new TwitterAccountsCtrl();
//console.log(ta.query());
