﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace DemoWebApp
{
    public partial class LoginPage : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnsubmit_Click(object sender, EventArgs e)
        {
            if(username.Value == "demo" && password.Value == "demopwd")
            Response.Redirect("/EmployeeList.aspx");
            else
            {
                Label1.Visible = true;
            }
        }
    }
}