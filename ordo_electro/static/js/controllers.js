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
	
	// activeSocialAccount --- stores the holder 
	$http({
		method : 'GET',
		url : '/social/accounts/'
	}).success(function(result) {
		$scope.socialAccounts = result;
	});

}

/**
 * twitter specific stuff 
 * @param $scope
 * @param $http
 */
function SocialAccountsCtrl($scope, $http) {
	$scope.twitterAccounts = [];
	
	// activeSocialAccount --- stores the holder 
	$http({
		method : 'GET',
		url : '/social/accounts/'
	}).success(function(result) {
		$scope.socialAccounts = result;
	});
}

function TwitterAccountCtrl($scope, $http) {
	
	// list of accounts assoicated to this users
	$http({
		method : 'GET',
		url : '/social/twitter/accounts/'
	}).success(function(result) {
		$scope.socialAccount = result;
	});
}


//For now I'll stuff this in here until I can get best practices 
//Define CreditCard class
var TwitterAccount = $resource('/social/twitter/accounts/:twitter_id', {
	twitter_id : '@id'
}, {
	update : {
		method : 'PUT'
	}
});


// We can retrieve a collection from the server
var cards = TwitterAccount.query(function() {
	// GET: /user/123/card
	// server returns: [ {id:456, number:'1234', name:'Smith'} ];

	var card = cards[0];
	// each item is an instance of CreditCard
	expect(card instanceof CreditCard).toEqual(true);
	card.name = "J. Smith";
	// non GET methods are mapped onto the instances
	card.$save();
	// POST: /user/123/card/456 {id:456, number:'1234', name:'J. Smith'}
	// server returns: {id:456, number:'1234', name: 'J. Smith'};

	// our custom method is mapped as well.
	card.$charge({
		amount : 9.99
	});
	// POST: /user/123/card/456?amount=9.99&charge=true {id:456, number:'1234', name:'J. Smith'}
});

angular
    .module('inspinia')
    .controller('MainCtrl', MainCtrl)
    .controller('SocialAccountsCtrl', SocialAccountsCtrl)
    .controller('TwitterAccountsCtrl', TwitterAccountsCtrl)
//    .factory('TwitterAccount',TwitterAccount)
    
