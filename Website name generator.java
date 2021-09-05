public class Website {
    int numUsers;
    String domain;
    String topLevelDomain;
    

    Website() {
        numUsers = 0;
        topLevelDomain = "com";
        domain = "";
    }
    
    Website(String d, String tld) {
        domain = d;
        topLevelDomain = tld;
        numUsers = 0;
    }
    
    Website(String d, String tld, int u) {
        domain = d;
        topLevelDomain = tld;
        numUsers = u;
    }
    
    public String toString()
    {
        String res =  "https://www." + domain + "." + topLevelDomain;
        res += " has " + numUsers + " users";
        
        return res;
    }
}    


// Tester/generator for Website class
public class WebsiteGenerator
{
    public static void main(String[] args)
    {
        Website w1 = new Website();
        System.out.println(w1);
        
        Website w2 = new Website("Google", "org");
        System.out.println(w2);
        
        Website w3 = new Website("Apple", "gov", 123324);
        System.out.println(w3);
        
    }
}

