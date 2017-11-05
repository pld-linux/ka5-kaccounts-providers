%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		kaccounts-providers
Summary:	KAccounts Providers
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3569f471743fddd167f353e1e698dd7e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KAccounts providers.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/signon-ui
%dir %{_sysconfdir}/signon-ui/webkit-options.d
%{_sysconfdir}/signon-ui/webkit-options.d/accounts.google.com.conf
%{_sysconfdir}/signon-ui/webkit-options.d/api.twitter.com.conf
%{_sysconfdir}/signon-ui/webkit-options.d/identi.ca.conf
%{_sysconfdir}/signon-ui/webkit-options.d/www.facebook.com.conf
%dir %{_libdir}/qt5/plugins/kaccounts
%dir %{_libdir}/qt5/plugins/kaccounts/ui
%attr(755,root,root) %{_libdir}/qt5/plugins/kaccounts/ui/owncloud_plugin_kaccounts.so
%{_datadir}/accounts
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.owncloud
%{_datadir}/metainfo/org.kde.kaccounts.owncloud.appdata.xml
