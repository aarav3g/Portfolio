public class WebsiteTester
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

