import requests
import re


html = '''
<!DOCTYPE html>
<!--[if IEMobile 7]><html class="iem7 oldie" lang="en"><![endif]-->
<!--[if (IE 7)&!(IEMobile)]><html class="ie7 oldie" lang="en"><![endif]-->
<!--[if (IE 8)&!(IEMobile)]><html class="ie8 oldie" lang="en"><![endif]-->
<!--[if (IE 9)&!(IEMobile)]><html class="ie9" lang="en"><![endif]-->
<!--[[if (gt IE 9)|(gt IEMobile 7)]><!--><html lang="en"><!--<![endif]-->
<!--
 * UBC CLF (Common Look and Feel) v7.0.2
 * Copyright 2012 The University of British Columbia
 * UBC Communications and Marketing
 * http://brand.ubc.ca/clf
 */
-->
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta charset="utf-8">
<title>CPSC 310 202 - Introduction to Software Engineering - UBC Student Services</title>
<meta name="viewport" content="width=device-width">
<meta name="description" content="">
<meta name="author" content="">
<!-- Stylesheets -->
<link href="/static/ubcclf/7.0.2/css/ubc-clf-full.min.css" rel="stylesheet">
<link href="/static/courseschedule/stylesheets/unit.css" rel="stylesheet">
<link href="/static/courseschedule/stylesheets/unit-responsive.css" rel="stylesheet">
<link href="/static/courseschedule/stylesheets/unit-print.css" rel="stylesheet">
<!--[if lte IE 7]>
<link href="/static/ubcclf/7.0.2/css/font-awesome-ie7.css" rel="stylesheet">
<![endif]-->
<!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
<!--[if lt IE 9]>
  <script src="/static/ubcclf/7.0.2/js/html5.js"></script>
<![endif]-->

<!-- Fav and touch icons -->
<link rel="shortcut icon" href="/static/ubcclf/7.0.2/img/favicon.ico">
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/ubcclf/7.0.2/img/apple-touch-icon-144-precomposed.png">
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/ubcclf/7.0.2/img/apple-touch-icon-114-precomposed.png">
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/ubcclf/7.0.2/img/apple-touch-icon-72-precomposed.png">
<link rel="apple-touch-icon-precomposed" href="/static/ubcclf/7.0.2/img/apple-touch-icon-57-precomposed.png">
<script src="/static/shared/scripts/jquery-1.8.1.min.js"></script>
</head>
<body>

<script type="text/javascript" src="/static/courseschedule/scripts/ttpopup.js"></script>

<div id="ttpopup" onmouseover="overdiv=1;"  onmouseout="overdiv=0; setTimeout('hideLayer()',1000)">
pop up description layer
</div>
    <div class="container">
        <!-- UBC Global Utility Menu -->
        <div class="collapse expand" id="ubc7-global-menu">
            <div id="ubc7-search" class="expand">
                <div id="ubc7-search-box">
                    <form class="form-search" method="get" action="http://www.ubc.ca/search/refine/" role="search">
                        <input type="search" name="q" placeholder="Search Course Schedule" class="input-xlarge search-query">
                        <input type="hidden" name="label" value="Search Course Schedule" />
                        <input type="hidden" name="site" value="courses.students.ubc.ca" />
                        <button type="submit" class="btn">Search</button>
                    </form>
                </div>
            </div>
            <div id="ubc7-global-header" class="expand">
                <!-- Global Utility Header from CDN -->
            </div>
        </div>
        <!-- End of UBC Global Utility Menu -->
        <!-- UBC Header -->
        <header id="ubc7-header" class="row-fluid expand" role="banner">
            <div class="span1">
                <div id="ubc7-logo">
                    <a href="http://www.ubc.ca" title="The University of British Columbia (UBC)">The University of British Columbia</a>
                </div>
            </div>
            <div class="span2">
                <div id="ubc7-apom">
                    <a href="https://cdn.ubc.ca/clf/ref/aplaceofmind" title="UBC a place of mind">UBC - A Place of Mind</a>
                </div>
            </div>
            <div class="span9" id="ubc7-wordmark-block">
                <div id="ubc7-wordmark">


                      <a href="http://www.ubc.ca" title="The University of British Columbia (UBC)">The University of British Columbia
                        <span class="ubc7-campus" id="ubc7-vancouver-campus">Vancouver campus </span>
                      </a>


                </div>
                <div id="ubc7-global-utility">
                    <button type="button" data-toggle="collapse" data-target="#ubc7-global-menu"><span>UBC Search</span></button>
                    <noscript><a id="ubc7-global-utility-no-script" href="http://www.ubc.ca/" title="UBC Search">UBC Search</a></noscript>
                </div>
            </div>
        </header>
        <!-- End of UBC Header -->
        <!-- UBC Unit Identifier -->
        <div id="ubc7-unit" class="row-fluid expand">
            <div class="span12">
                <!-- Mobile Menu Icon -->
                <div class="navbar">
                    <a class="btn btn-navbar" data-toggle="collapse" data-target="#ubc7-unit-navigation">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </a>
                </div>
                <!-- Read more about Course Schedule Treatment on http://brand.ubc.ca/clf -->
                <!-- No Faculty Treatment --><!--<div id="ubc7-unit-name" class="ubc7-single-element"> -->
                <div id="ubc7-unit-name">

                   <a href="/cs/courseschedule?pname=welcome&tname=welcome" title="Course Schedule"><span id="ubc7-unit-faculty">Student Service Centre</span><span id="ubc7-unit-identifier">Course Schedule</span></a>


                </div>
            </div>
        </div>
        <!-- End of UBC Unit Identifier -->


        <!-- UBC Unit Navigation --> <div id='ubc7-unit-menu' class='navbar expand' role='navigation'> <div class='navbar-inner expand'><div class='container'><div class='nav-collapse collapse' id='ubc7-unit-navigation'><ul class='nav'> <li class='dropdown Browse'>  <div class='btn-group'>  <a class='btn' data-toggle='dropdown' >Browse  <div class='ubc7-arrow down-arrow'></div></a>  <ul class='dropdown-menu'> <li class='Standard_Timetables' ><a href='/cs/courseschedule?pname=stt&amp;tname=stt' title='Standard Timetables'>Standard Timetables</a></li> <li class='Browse_Courses' ><a href='/cs/courseschedule?pname=subjarea&amp;tname=subj-all-departments' title='Courses'>Courses</a></li> <li class='Browse_Specializations' ><a href='/cs/courseschedule?pname=spec&amp;tname=spec' title='Specializations'>Specializations</a></li>  </ul>  </div>  </li>  <li class='dropdown Search'>  <div class='btn-group'>  <a class='btn' data-toggle='dropdown' >Search  <div class='ubc7-arrow down-arrow'></div></a>  <ul class='dropdown-menu'> <li class='Search_Courses' ><a href='/cs/courseschedule?pname=subjarea&amp;tname=sectsearch' title='Courses'>Courses</a></li> <li class='Search_Instructor' ><a href='/cs/courseschedule?pname=instsearch&amp;tname=instsearch' title='Instructor'>Instructor</a></li>  </ul>  </div>  </li>  <li class='dropdown Help'>  <div class='btn-group'>  <a class='btn'  data-toggle='dropdown'>Help  <div class='ubc7-arrow down-arrow'></div></a>  <ul class='dropdown-menu'>  <li class='Quick_Help'><a href='/static/courseschedule/cs_quick_help.htm' title='Quick Help' target='_blank'>Quick Help</a></li>  <li class='Glossary'><a href='/static/courseschedule/cs_glossary.htm' title='Glossary' target='_blank'>Glossary</a></li>  <li class='Planning_UBCV'><a href='http://www.calendar.ubc.ca/vancouver/planning.cfm' title='Course Planning - Vancouver' target='_blank'>Course Planning - Vancouver</a></li>  <li class='Planning_UBCO'><a href='http://www.calendar.ubc.ca/okanagan/index.cfm?tree=18,0,0,0' title='Course Planning - Okanagan' target='_blank'>Course Planning - Okanagan</a></li>  </ul>  </div>  </li> </ul> <div id='cwl' class='pull-right'><form action='/cs/secure/login' method='GET'> <input type='IMAGE' name='IMGSUBMIT' value='IMGSUBMIT' src='https://www.auth.cwl.ubc.ca/CWL_login_button.gif' WIDTH='76' HEIGHT='25' ALT='CWL Login' BORDER='0' /> </form> </div></div><!-- /.nav-collapse -->  </div>  </div><!-- /navbar-inner -->  </div><!-- /navbar -->  <!-- End of UBC Unit Navigation -->




            <!-- UBC Unit Breadcrumbs --> <ul class='breadcrumb expand'> <li><a href=/cs/courseschedule?pname=welcome&amp;tname=welcome title='Course Schedule'>Course Schedule</a> <span class='divider'>/</span> </li> <li><a href="/cs/courseschedule;jsessionid=i5e4AycKRCUSQgl2DHYzRN6d?pname=subjarea&amp;tname=subj-all-departments">Browse Courses</a> <span class='divider'>/</span> </li><li><a href="/cs/courseschedule;jsessionid=i5e4AycKRCUSQgl2DHYzRN6d?pname=subjarea&amp;tname=subj-department&amp;dept=CPSC">CPSC</a> <span class='divider'>/</span> </li><li><a href="/cs/courseschedule;jsessionid=i5e4AycKRCUSQgl2DHYzRN6d?pname=subjarea&amp;tname=subj-course&amp;dept=CPSC&amp;course=310">CPSC 310</a> <span class='divider'>/</span> </li><li class='active' >CPSC 310 202</li> <div class='pull-right'> <div class='btn-group'><button class='btn btn-primary' data-toggle='dropdown'>Campus: UBC Vancouver</button>  <button class='btn btn-primary dropdown-toggle' data-toggle='dropdown'><i class='icon-chevron-down'></i></button> <ul class='dropdown-menu'> <li class='active' ><a href='/cs/courseschedule?tname=subj-section&course=310&section=202&campuscd=UBC&dept=CPSC&pname=subjarea' title='UBC'>UBC Vancouver</a></li> <li><a href='/cs/courseschedule?tname=subj-section&course=310&section=202&campuscd=UBCO&dept=CPSC&pname=subjarea' title='UBCO'>UBC Okanagan</a></li> </ul></div><div class='btn-group'><button class='btn btn-primary' data-toggle='dropdown'>Session: 2019 Winter</button>  <button class='btn btn-primary dropdown-toggle' data-toggle='dropdown'><i class='icon-chevron-down'></i></button> <ul class='dropdown-menu'> <li><a href='/cs/courseschedule?sesscd=S&pname=subjarea&tname=subj-section&course=310&sessyr=2019&section=202&dept=CPSC' title='2019 Summer'>2019 Summer</a></li> <li><a href='/cs/courseschedule?sesscd=W&pname=subjarea&tname=subj-section&course=310&sessyr=2018&section=202&dept=CPSC' title='2018 Winter'>2018 Winter</a></li> <li class='active' ><a href='/cs/courseschedule?sesscd=W&pname=subjarea&tname=subj-section&course=310&sessyr=2019&section=202&dept=CPSC' title='2019 Winter'>2019 Winter</a></li> </ul></div></div> </ul> <!-- End of UBC Unit Breadcrumbs -->




        <!-- Content Area -->
        <div class="content expand" role="main">
        <br/>
          <!-- Main Content-->








































        <a class="btn btn-small pull-right margin-left btn-primary btn-disabled">Save To Worklist</a>






    <h4>CPSC 310 202 (Lecture)</h4><h5>Introduction to Software Engineering</h5><p>Specification, design, implementation and maintenance of large, multi-module software systems. Principles, techniques, methodologies and tools for computer aided software engineering (CASE); human-computer interfaces, reactive systems, hardware-software interfaces and distributed applications.</p><div class="alert alert-info" id="cdfText"><b>This course is eligible for Credit/D/Fail grading.</b> To determine whether you can take this course for Credit/D/Fail grading, visit the <a href=https://students.ubc.ca/enrolment/courses/creditdfail-grading target="_blank">Credit/D/Fail</a> website. You must register in the course before you can select the Credit/D/Fail grading option. </div><p>Credits:  4</p><p>Location:  Vancouver<br/></p><b>Term 2</b> (Jan 06, 2020 to Apr 08, 2020)<br/><b></b><br/><div class="alert alert-info" id="cdfText"><p><strong>Cr/D/F Grading Change Dates</strong></p><p>Last day to change between Credit/D/Fail and percentage grading (grading options cannot be changed after this date): <strong>January 17, 2020</strong></p></div><br /> <table class="table table-nonfluid"><thead><tr><th colspan='2'>Withdrawal Dates</th></tr></thead><tr><td>Last day to withdraw without a W standing : </td><td><b>January 17, 2020</b></td></tr><tr><td>Last day to withdraw with a W standing <br/>(course cannot be dropped after this date) : </td><td><b>February 14, 2020</b></td></tr></table><br/><table class="table  table-striped"><thead><tr><th>Term</th><th>Day</th> <th>Start Time</th><th>End Time</th><th>Building</th><th>Room</th></tr></thead><td>2</td><td> Mon Wed Fri</td><td>15:00</td><td>16:00</td><td>MacMillan</td><td><a href=https://ssc.adm.ubc.ca/classroomservices/function/viewlocation?userEvent=ShowLocation&amp;buildingID=MCML&amp;roomID=166 target="_blank">166</a></td></table><table class="table"><tr><td>Instructor:  </td><td><a href="/cs/courseschedule?pname=inst&amp;ubcid=1502491&amp;catano=7181&amp;term=2&amp;sessyr=2019&amp;sesscd=W&amp;campuscd=UBC&amp;dept=CPSC&amp;course=310&amp;section=202">BANIASSAD, ELISA</a></td></tr></table><strong>Note: this section is full</strong><br/><br/><table class=&#39;table table-nonfluid&#39;>
<thead><th colspan=&#39;2&#39;><strong>Seat Summary</strong></th></thead>
<tr><td width=&#39;200px&#39;>Total Seats Remaining:</td><td align=&#39;left&#39;><strong>0</strong></td></tr>
<tr><td width=&#39;200px&#39;>Currently Registered:</td><td align=&#39;left&#39;><strong>158</strong></td></tr>
<tr><td width=&#39;200px&#39;>General Seats Remaining:</td><td align=&#39;left&#39;><strong>0</strong></td></tr>
<tr><td width=&#39;200px&#39;>Restricted Seats Remaining*:</td><td align=&#39;left&#39;><strong>0</strong></td></tr>
<tr><TD colspan=&#39;2&#39;>&nbsp;&nbsp;&nbsp;&nbsp;*These seats are reserved for students who meet one of the following sets of restrictions:<TABLE width=100% border=0 cellspacing=0 cellpadding=1><TR><TD width=3%>&nbsp;</TD><TD><OL type=1><LI>with one of these specializations: ****SENG
</LI>
<LI>in one of these programs: BCS
-OR-<br>
in year: >=3
with one of these specializations: CHN CPSC,CMJ CPSC,HON CPSC,MAJ CPSC
-OR-<br>
in year: >=3
with one of these specializations: ****COMI
-OR-<br>
in year: >=3
with one of these specializations: ****BUCS,****BUCC
</LI>
</UL></TD></TR></TABLE></TD></TR>
</table>



-&nbsp;
Select one Laboratory from sections L2A, L2B, L2C, L2D, L2E, L2F, L2G, L2H, L2J, L2K, L2M, L2N, L2P, L2R, L2S
<br/>











<br/>
<b>Book Summary</b> <a href=http://www.bookstore.ubc.ca/textbooks/ target=_blank       onmouseover=displayHelpText(Information about the book list.,235,160,event,Book List)       onmouseout=closePopup();><i class='icon-question-sign'></i></a>:  <table class='sortable table table-striped'> <tr> <td>Information for the books required for this section is not available.</td></tr></table>


          <!-- end of Main Content -->

        &nbsp;
        </div>
        <!-- End of Content Area -->



       <!-- Footer Area Unit Menu - Mobile Only --><div id='ubc7-unit-alternate-navigation' class='navbar expand visible-phone' role='navigation'> <div class='navbar-inner expand'><div class='container'><div class='nav-collapse collapse'><ul class='nav'> <li class='dropdown Browse'>  <div class='btn-group'>  <a class='btn' data-toggle='dropdown' >Browse  <div class='ubc7-arrow down-arrow'></div></a>  <ul class='dropdown-menu'> <li class='Standard_Timetables' ><a href='/cs/courseschedule?pname=stt&amp;tname=stt' title='Standard Timetables'>Standard Timetables</a></li> <li class='Browse_Courses' ><a href='/cs/courseschedule?pname=subjarea&amp;tname=subj-all-departments' title='Courses'>Courses</a></li> <li class='Browse_Specializations' ><a href='/cs/courseschedule?pname=spec&amp;tname=spec' title='Specializations'>Specializations</a></li>  </ul>  </div>  </li>  <li class='dropdown Search'>  <div class='btn-group'>  <a class='btn' data-toggle='dropdown' >Search  <div class='ubc7-arrow down-arrow'></div></a>  <ul class='dropdown-menu'> <li class='Search_Courses' ><a href='/cs/courseschedule?pname=subjarea&amp;tname=sectsearch' title='Courses'>Courses</a></li> <li class='Search_Instructor' ><a href='/cs/courseschedule?pname=instsearch&amp;tname=instsearch' title='Instructor'>Instructor</a></li>  </ul>  </div>  </li>  <li class='dropdown Help'>  <div class='btn-group'>  <a class='btn'  data-toggle='dropdown'>Help  <div class='ubc7-arrow down-arrow'></div></a>  <ul class='dropdown-menu'>  <li class='Quick_Help'><a href='/static/courseschedule/cs_quick_help.htm' title='Quick Help' target='_blank'>Quick Help</a></li>  <li class='Glossary'><a href='/static/courseschedule/cs_glossary.htm' title='Glossary' target='_blank'>Glossary</a></li>  <li class='Planning_UBCV'><a href='http://www.calendar.ubc.ca/vancouver/planning.cfm' title='Course Planning - Vancouver' target='_blank'>Course Planning - Vancouver</a></li>  <li class='Planning_UBCO'><a href='http://www.calendar.ubc.ca/okanagan/index.cfm?tree=18,0,0,0' title='Course Planning - Okanagan' target='_blank'>Course Planning - Okanagan</a></li>  </ul>  </div>  </li> </ul> <div id='cwl' class='pull-right'><form action='/cs/secure/login' method='GET'> <input type='IMAGE' name='IMGSUBMIT' value='IMGSUBMIT' src='https://www.auth.cwl.ubc.ca/CWL_login_button.gif' WIDTH='76' HEIGHT='25' ALT='CWL Login' BORDER='0' /> </form> </div></div><!-- /.nav-collapse -->  </div>  </div><!-- /navbar-inner -->  </div><!-- /navbar -->  <!-- End of Footer Area Unit Menu -->



         <div id="dwindow" style="position: fixed; background-color: rgb(235, 235, 235); display: none;border-width:medium;border-style:solid; z-index:99;">
            <div><p id="dwindowTitle" class='formHeader' align='left' style='margin-top:0;margin-bottom:0'><b>Comments</b></p></div>
            <div>
            <table><tr><td id="helpContent">&nbsp;</td></tr></table>
            </div>
          </div>

          <div class="fullscreen" id="processingOverlay" style="display:none">
                        <div class="centerbox" id="processingText">
                        <div style="text-align: center;"><b>Please wait while your request is processed - this may take up to a minute to complete.</b></div>
                        <table align="center"><tr><td>
                        <div style="font-size:6pt;padding:2px;border:solid black 1px">
                        <span id="box1">&nbsp; &nbsp;</span>
                        <span id="box2">&nbsp; &nbsp;</span>
                        <span id="box3">&nbsp; &nbsp;</span>
                        <span id="box4">&nbsp; &nbsp;</span>
                        <span id="box5">&nbsp; &nbsp;</span>
                        <span id="box6">&nbsp; &nbsp;</span>
                        <span id="box7">&nbsp; &nbsp;</span>
                        <span id="box8">&nbsp; &nbsp;</span>
                        <span id="box9">&nbsp; &nbsp;</span>
                        <span id="box10">&nbsp; &nbsp;</span>
                        <span id="box11">&nbsp; &nbsp;</span>
                        </div>
                        </td></tr>
                        </table>

                        </div>
                    </div>

        <footer id="ubc7-footer" class="expand" role="contentinfo">
            <div class="row-fluid expand" id="ubc7-unit-footer">
                <div class="span10" id="ubc7-unit-address">


                    <div id="ubc7-address-location">
                        <span id="ubc7-address-city">Vancouver | Kelowna</span>, <span id="ubc7-address-province" title="British Columbia">BC</span> <span id="ubc7-address-country">Canada</span>
                    </div>

                      <div id="ubc7-address"><a href="https://www.askme.ubc.ca/" target="_blank">Contact Us</a></div>


                </div>
                <div class="span2">
                    <strong>Find us on</strong>
                    <div id="ubc7-unit-social-icons">
                        <a href="https://www.facebook.com/universityofbc?fref=ts" title="Facebook icon"><i class="icon-facebook-sign"></i></a>&nbsp;
                        <a href="https://twitter.com/ubc " title="Twitter icon"><i class="icon-twitter-sign"></i></a>
                    </div>
                </div>
            </div>
            <div class="row-fluid expand ubc7-back-to-top">
                <div class="span2">
                    <a href="#" title="Back to top">Back to top <div class="ubc7-arrow up-arrow grey"></div></a>
                </div>
            </div>
            <div class="row-fluid expand" id="ubc7-global-footer">
                <div class="span5" id="ubc7-signature"><a href="http://www.ubc.ca/" title="The University of British Columbia (UBC)">The University of British Columbia</a></div>
                <div class="span7" id="ubc7-footer-menu">
                </div>
            </div>
            <div class="row-fluid expand" id="ubc7-minimal-footer">
                <div class="span12">
                    <ul>
                        <li><a href="https://cdn.ubc.ca/clf/ref/emergency" title="Emergency Procedures">Emergency Procedures</a> <span class="divider">|</span></li>
                        <li><a href="https://cdn.ubc.ca/clf/ref/terms" title="Terms of Use">Terms of Use</a> <span class="divider">|</span></li>
                        <li><a href="https://cdn.ubc.ca/clf/ref/copyright" title="UBC Copyright">Copyright</a> <span class="divider">|</span></li>
                        <li><a href="https://cdn.ubc.ca/clf/ref/accessibility" title="Accessibility">Accessibility</a></li>
                    </ul>
                </div>
            </div>
        </footer>

    </div> <!-- /container -->
    <!-- Placed javascript at the end for faster loading -->
    <script src="/static/ubcclf/7.0.2/js/ubc-clf.min.js"></script>

    <script language="JavaScript" src="/static/shared/scripts/tablesorter.js"></script>
    <script language="JavaScript" src="/static/shared/scripts/tablefilter.js"></script>
    <script language="JavaScript" src="/static/courseschedule/scripts/simplePopup.js"></script>
    <script language="JavaScript" src="/static/courseschedule/scripts/dhtml_pos.js"></script>
    <script type="text/javascript" src="/static/courseschedule/scripts/unit.js"></script>
    <script type="text/javascript" src="/static/courseschedule/scripts/validate.js"></script>
    <script type="text/javascript" src="/static/courseschedule/scripts/columnsToRows.js"></script>
    <script type="text/javascript">
      <!-- // Automatic redirection based on form selection
      function redirect_header() {
        goTo = document.form_header.select_links.options[document.form_header.select_links.selectedIndex].value;
        if (goTo != "") {
          location = goTo;
        }
      }
      // -->
    </script>
    <script type="text/javascript" src="/static/shared/scripts/coursesanalytics.js"></script>
        <script type="text/javascript">
            var progressEnd = 11;           // set to number of progress <span>'s.
            var progressColor = '#002145';  // set to progress bar color
            var progressInterval = 200;     // set to time between updates (milli-seconds)
            var color = progressColor;

            var progressAt = progressEnd;
            var progressTimer;

            function progress_update() {
                    progressAt++;
                    if (progressAt > progressEnd) {
                      progressAt = 1;
                      if (color == progressColor) {
                        color = 'transparent';
                      } else {
                        color = progressColor;
                      }
                    }
                    document.getElementById('box'+progressAt).style.backgroundColor = color;
                    progressTimer = setTimeout('progress_update()',progressInterval);
            }
            progress_update();              // start progress bar
        </script>
</body>
</html>

'''


pattern = re.compile(r'(?<=left&\S39;><strong>).*?(?=</strong></td></tr>)')
matches = pattern.finditer(html)

for match in matches:
	print (match)







