/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.cfg.Configuration;
/**
 *
 * @author Vishwakarma
 */
public class StoreData {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
         Configuration cfg = new Configuration();
        cfg.configure("hibernate.cfg.xml");
        StandardServiceRegistryBuilder ssr = new StandardServiceRegistryBuilder().applySettings(cfg.getProperties());
        SessionFactory factory = cfg.buildSessionFactory(ssr.build());
        
        // Open session and transaction
        Session session = factory.openSession();
        Transaction t = session.beginTransaction();
        
        // Create Employee object and save it
        Employee e1 = new Employee();
        e1.setId(2);
        e1.setFirstName("suraj");
        e1.setLastName("vishwakarma");

        session.save(e1);
        t.commit();

        System.out.println("Successfully saved");
        session.close();
        factory.close();
    }
    
}
