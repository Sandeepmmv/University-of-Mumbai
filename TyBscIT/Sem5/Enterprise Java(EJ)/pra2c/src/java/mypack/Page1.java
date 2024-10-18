/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mypack;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpSession;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author Vishwakarma
 */
@WebServlet(name = "Page1", urlPatterns = {"/Page1"})
public class Page1 extends HttpServlet {
public void doGet(HttpServletRequest request, HttpServletResponse response)
throws ServletException, IOException {
response.setContentType("text/html;charset=UTF-8");
PrintWriter out = response.getWriter();
out.println("<html><head><title>Servlet Page1</title></head>");
HttpSession hs = request.getSession(true);
if(hs.isNew()){
out.println("<body bgcolor=yellow>");
String name = request.getParameter("txtName");
hs.setAttribute("uname", name);
hs.setAttribute("visit", "1");
out.println("<h1>Welcome First Time</h1>");
}
else{
out.println("<h1>Welcome Again</h1>");
int visit = Integer.parseInt((String)hs.getAttribute("visit"))+1;
out.println("<h1>You Visited "+visit+"Times</h1>");
hs.setAttribute("visit", ""+visit);
}
out.println("<h1>Your Session ID "+hs.getId()+"</h1>");
out.println("<h1>You Logged in at "+new java.util.Date(hs.getCreationTime())+"</h1>");
out.println("<h1><a href=Page2>Click for Page 2 </a></h1>");
out.println("<h1><a href=Page3>Click for Page 3 </a></h1>");    
out.println("<h1><a href=Page4>Click for Page 4 </a></h1>");
out.println("<h1><a href=LogoutServlet>Click to Terminate Session </a></h1>");
out.println("</body>");
out.println("</html>");
}
}