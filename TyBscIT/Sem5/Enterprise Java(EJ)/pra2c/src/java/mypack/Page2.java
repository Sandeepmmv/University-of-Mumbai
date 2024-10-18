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
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author Vishwakarma
 */
@WebServlet(name = "Page2", urlPatterns = {"/Page2"})
public class Page2 extends HttpServlet {
public void doGet(HttpServletRequest request, HttpServletResponse response)
throws ServletException, IOException {
response.setContentType("text/html;charset=UTF-8");
PrintWriter out = response.getWriter();
out.println("<html><head><title>Servlet Page2</title></head>");
HttpSession hs = request.getSession(false);
out.println("<h1>Welcome Again on Page No. 2</h1>");
int visit = Integer.parseInt((String)hs.getAttribute("visit"))+1;
out.println("<h1>You Visited "+visit+"Times</h1>");
hs.setAttribute("visit", ""+visit);
out.println("<h1>Your Session ID "+hs.getId()+"</h1>");
out.println("<h1>You Logged in at "+new java.util.Date(hs.getCreationTime())+"</h1>");
out.println("<h1><a href=Page1>Click for Page 1 </a></h1>");
out.println("<h1><a href=Page3>Click for Page 3 </a></h1>");
out.println("<h1><a href=Page4>Click for Page 4 </a></h1>");
out.println("<h1><a href=LogoutServlet>Click for Terminate Session </a></h1>");
out.println("</body>");
out.println("</html>");
}
}