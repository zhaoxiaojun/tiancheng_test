<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" version="1.0" encoding="gb2312" indent="yes" />
	
	<xsl:template match="/">
		<HTML>
			<head>
				<title>天秤WebUI自动化测试用例</title>
			</head>
			<BODY topmargin="0">
				<table id="Table_01" width="100%" height="49" border="0" cellpadding="0" cellspacing="0">
					<tr>
						<td width="687" height="49">
							<table width="687" height="49" >
								<tr>
									<td></td>
								</tr>
							</table>
						</td>
						<td width="100%" align="right">
							<font style="font-family:Arial;font-size:12px;position:relative;right:130px;">
								NiiWoo TianCheng WebUI AutoTest
								<br />
								天秤测试
							</font>
						</td>
					</tr>
				</table>
				
				<h5>测试环境信息:</h5>
				<br />
				<h2><xsl:value-of select="setting"/></h2>
				
				<xsl:for-each select="testsuite/testcase">
					<br />
					<font color="green">
						<center>
							用例名称: <xsl:value-of select="@name" />
						</center>
					</font>
					<br />
					
					<xsl:for-each select="steps">
						<br />
						<TABLE width="90%" cellspacing="1" cellpadding="1" ALIGN="CENTER">
							<TBODY>
								<TR bgcolor="#00e2df">
									<td></td>
									<td></td>
									<td></td>
									<td></td>
									<td></td>
								</TR>
								<TR bgcolor="#d7e2da">
									<TH>
										<font size="2.5">步骤编号</font>
									</TH>
									<TH>
										<font size="2.5">步骤类型</font>
									</TH>
									<TH>
										<font size="2.5">步骤名称</font>
									</TH>
									<TH>
										<font size="2.5">期望结果</font>
									</TH>
									<TH>
										<font size="2.5">实际结果</font>
									</TH>
								</TR>
								<xsl:for-each select="step">
									<TR>
										<TD>
											step
										</TD>
										<TD>
										</TD>
										<TD>
										</TD>
										<TD>
										</TD>
										<TD>
										</TD>
									</TR>
								</xsl:for-each>
								<!--step -->
							</TBODY>
						</TABLE>
					</xsl:for-each>
					<!--STEPS -->
					<br />
					<br />
				</xsl:for-each>
			</BODY>
		</HTML>
	</xsl:template>
</xsl:stylesheet>