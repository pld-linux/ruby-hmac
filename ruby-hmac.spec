%define gem_name ruby-hmac
Summary:	An implementation of the HMAC authentication code in Ruby
Name:		ruby-hmac
Version:	0.4.0
Release:	2
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/topfunky-%{name}-v%{version}-0-ga401a7d.tar.gz
# Source0-md5:	675592bc7db5fc4cb456a0c38135779b
URL:		http://ruby-hmac.rubyforge.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Provides:	ruby-ruby-hmac = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides common interface to HMAC functionality. HMAC is a
kind of "Message Authentication Code" (MAC) algorithm whose standard
is documented in RFC2104. Namely, a MAC provides a way to check the
integrity of information transmitted over or stored in an unreliable
medium, based on a secret key. Originally written by Daiki Ueno.
Converted to a RubyGem by Geoffrey Grosenbach

%prep
%setup -qc
mv topfunky-ruby-hmac-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt History.txt
%{ruby_vendorlibdir}/hmac.rb
%{ruby_vendorlibdir}/hmac-md5.rb
%{ruby_vendorlibdir}/hmac-rmd160.rb
%{ruby_vendorlibdir}/hmac-sha1.rb
%{ruby_vendorlibdir}/hmac-sha2.rb
%{ruby_vendorlibdir}/ruby_hmac.rb
