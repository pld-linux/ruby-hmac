
%define gitrev a401a7d
%define gitauthor topfunky
%define gitname ruby-hmac

Summary:	An implementation of the HMAC authentication code in Ruby
Name:		ruby-hmac
Version:	0.4.0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/%{gitauthor}-%{gitname}-v%{version}-0-g%{gitrev}.tar.gz
# Source0-md5:	675592bc7db5fc4cb456a0c38135779b
#Patch0: %{name}-nogems.patch
URL:		http://ruby-hmac.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.4.1
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-hmac
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of the HMAC authentication code in Ruby, originally
from Daiki Ueno

%prep
%setup -q -n %{gitauthor}-%{gitname}-%{gitrev}
#%patch0 -p1
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/hmac.rb
%{ruby_rubylibdir}/hmac-md5.rb
%{ruby_rubylibdir}/hmac-rmd160.rb
%{ruby_rubylibdir}/hmac-sha1.rb
%{ruby_rubylibdir}/hmac-sha2.rb
%{ruby_rubylibdir}/ruby_hmac.rb
