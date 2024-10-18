/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import java.util.Iterator;
import java.util.List;

public class ManageCourse {
    private static SessionFactory factory;

    public static void main(String[] args) {
        try {
            factory = new Configuration().configure().buildSessionFactory();
        } catch (Throwable ex) {
            System.err.println("Failed to create sessionFactory object." + ex);
            throw new ExceptionInInitializerError(ex);
        }

        ManageCourse mc = new ManageCourse();

        /* Add few course records in the database */
        Integer courseID1 = mc.addCourse("Java", 10000);
        Integer courseID2 = mc.addCourse("python", 10000);

        /* List down all courses */
        mc.listCourses();

        /* Update course records */
        mc.updateCourse(courseID2, 5000);

        /* Delete a course record from the database */
        mc.deleteCourse(courseID1);

        /* List down new list of courses */
        mc.listCourses();
    }

    /* Method to CREATE a course in the database */
    public Integer addCourse(String CName, int fees) {
        Session session = factory.openSession();
        org.hibernate.Transaction tx = null;
        Integer courseID = null;
        try {
            tx = session.beginTransaction();
            Course course = new Course(CName, fees);
            courseID = (Integer) session.save(course);
            tx.commit();
        } catch (HibernateException e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
        } finally {
            session.close();
        }
        return courseID;
    }

    /* Method to READ all the courses */
    public void listCourses() {
        Session session = factory.openSession();
        org.hibernate.Transaction tx = null;
        try {
            tx = session.beginTransaction();
            List courses = session.createQuery("FROM Course").list();
            for (Iterator iterator = courses.iterator(); iterator.hasNext(); ) {
                Course course = (Course) iterator.next();
                System.out.print("Course Name: " + course.getCName());
                System.out.println("  Fees: " + course.getFees());
            }
            tx.commit();
        } catch (HibernateException e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
        } finally {
            session.close();
        }
    }

    /* Method to UPDATE course fees */
    public void updateCourse(Integer courseID, int fees) {
        Session session = factory.openSession();
        org.hibernate.Transaction tx = null;
        try {
            tx = session.beginTransaction();
            Course course = (Course) session.get(Course.class, courseID);
            course.setFees(fees);
            session.update(course);
            tx.commit();
        } catch (HibernateException e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
        } finally {
            session.close();
        }
    }

    /* Method to DELETE a course from the records */
    public void deleteCourse(Integer courseID) {
        Session session = factory.openSession();
        org.hibernate.Transaction tx = null;
        try {
            tx = session.beginTransaction();
            Course course = (Course) session.get(Course.class, courseID);
            session.delete(course);
            tx.commit();
        } catch (HibernateException e) {
            if (tx != null) tx.rollback();
            e.printStackTrace();
        } finally {
            session.close();
        }
    }
}

