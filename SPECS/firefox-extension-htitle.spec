Name:           firefox-extension-htitle
Version:        3.4.1
Release:        1%{?dist}
Summary:        HTitle extension for Firefox

Group:          Applications/Internet
License:        MPLv2.0
URL:            https://github.com/seleznev/firefox-extension-htitle

# Signed XPI downloded from https://addons.mozilla.org/en-US/firefox/addon/htitle/
Source0:        firefox-extension-htitle-3.4.1.xpi

BuildArch:      noarch
Requires:       firefox

%description
Extension for Firefox that hides the title bar if window is maximized.

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/firefox/browser/extensions/
cp -p %SOURCE0 $RPM_BUILD_ROOT/%{_libdir}/firefox/browser/extensions/\{c6448328-31f7-4b12-a2e0-5c39d0290307\}.xpi

%files
%defattr(-,root,root,-)
%{_libdir}/firefox/browser/extensions/*.xpi

%changelog
* Sat Dec 17 2016 Ricardo Arguello <rarguello@deskosproject.org> - 3.4.1-1
- Initial release for DeskOS
