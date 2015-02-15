var twitterAccountServices = angular.module('twitterAccountServices',
		[ 'ngResource' ]);

twitterAccountServices.factory('TwitterAccount', [ '$resource',
		function($resource) {
			return $resource('social/:twitter_id.json', {}, {
				query : {
					method : 'GET',
					params : {
						twitter_id : 'accounts'
					},
					isArray : true
				}
			});
		} ]);
