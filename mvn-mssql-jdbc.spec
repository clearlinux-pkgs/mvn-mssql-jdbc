#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-mssql-jdbc
Version  : 6.2.1
Release  : 2
URL      : https://github.com/microsoft/mssql-jdbc/archive/v6.2.1.tar.gz
Source0  : https://github.com/microsoft/mssql-jdbc/archive/v6.2.1.tar.gz
Source1  : https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/6.2.1.jre7/mssql-jdbc-6.2.1.jre7.jar
Source2  : https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/6.2.1.jre7/mssql-jdbc-6.2.1.jre7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 MIT
Requires: mvn-mssql-jdbc-data = %{version}-%{release}

%description
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/Microsoft/mssql-jdbc/master/LICENSE)
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/com.microsoft.sqlserver/mssql-jdbc/badge.svg)](http://mvnrepository.com/artifact/com.microsoft.sqlserver/mssql-jdbc)
[![Javadocs](http://javadoc.io/badge/com.microsoft.sqlserver/mssql-jdbc.svg)](http://javadoc.io/doc/com.microsoft.sqlserver/mssql-jdbc)
[![Gitter](https://img.shields.io/gitter/room/badges/shields.svg)](https://gitter.im/Microsoft/mssql-developers)
</br>
# Microsoft JDBC Driver for SQL Server

%package data
Summary: data components for the mvn-mssql-jdbc package.
Group: Data

%description data
data components for the mvn-mssql-jdbc package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/microsoft/sqlserver/mssql-jdbc/6.2.1.jre7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/microsoft/sqlserver/mssql-jdbc/6.2.1.jre7/mssql-jdbc-6.2.1.jre7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/microsoft/sqlserver/mssql-jdbc/6.2.1.jre7
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/microsoft/sqlserver/mssql-jdbc/6.2.1.jre7/mssql-jdbc-6.2.1.jre7.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/microsoft/sqlserver/mssql-jdbc/6.2.1.jre7/mssql-jdbc-6.2.1.jre7.jar
/usr/share/java/.m2/repository/com/microsoft/sqlserver/mssql-jdbc/6.2.1.jre7/mssql-jdbc-6.2.1.jre7.pom
