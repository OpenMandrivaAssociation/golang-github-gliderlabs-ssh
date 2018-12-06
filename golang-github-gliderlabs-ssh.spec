# Run tests in check section
%bcond_without check

%global goipath         github.com/gliderlabs/ssh
Version:                0.1.1

%global common_description %{expand:
This Go package wraps the crypto/ssh package with a higher-level API for 
building SSH servers. The goal of the API was to make it as simple as 
using net/http, so the API is very similar.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        Easy SSH servers in Golang
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/anmitsu/go-shlex)
BuildRequires: golang(golang.org/x/crypto/ssh)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.1-1
- Bump to 0.1.1

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-0.1-20180421git8c17077
- First package for Fedora

