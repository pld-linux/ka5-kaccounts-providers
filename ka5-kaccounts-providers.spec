%define		kdeappsver	21.08.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kaccounts-providers
Summary:	KAccounts Providers
Name:		ka5-%{kaname}
Version:	21.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0a97e8fa7f27111ae78b5e05f308bb76
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	ka5-kaccounts-integration-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	libaccounts-glib-devel
BuildRequires:	libaccounts-qt5-devel
BuildRequires:	libsignon-qt5-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Accounts Providers.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
%attr(755,root,root) %{_libdir}/qt5/plugins/kaccounts/ui/nextcloud_plugin_kaccounts.so
%{_iconsdir}/hicolor/256x256/apps/kaccounts-owncloud.png
%{_iconsdir}/hicolor/scalable/apps/kaccounts-nextcloud.svg
%dir %{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud
%dir %{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/contents
%dir %{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/contents/ui
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/contents/ui/Server.qml
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/contents/ui/Services.qml
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/contents/ui/WebLogin.qml
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/contents/ui/main.qml
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/metadata.desktop
%{_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/metadata.json
%{_datadir}/metainfo/org.kde.kaccounts.nextcloud.appdata.xml
