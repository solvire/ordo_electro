from dateutil import parser

class Mapper:
    
    @staticmethod
    def bindJson(profile,twitter_account):
        skips =  ['id']
        
        """
        Map a json obect to a TwitterAccount
        """
        for key,value in profile.iteritems():
            # check to see if it exists by force 
            try:
                twitter_account._meta.get_field_by_name(key)
            except:
                continue
            if key in skips: continue
            if key == 'created_at': 
                twitter_account.created_at = parser.parse(value)
                continue
            
            setattr(twitter_account, key, value)
        return twitter_account
            
            
        