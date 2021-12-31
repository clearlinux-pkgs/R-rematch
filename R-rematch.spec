#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rematch
Version  : 1.0.1
Release  : 37
URL      : https://cran.r-project.org/src/contrib/rematch_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rematch_1.0.1.tar.gz
Summary  : Match Regular Expressions with a Nicer 'API'
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
captured groups from the match of a regular expression to a character
    vector.

%prep
%setup -q -c -n rematch
cd %{_builddir}/rematch

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589510252

%install
export SOURCE_DATE_EPOCH=1589510252
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rematch
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rematch
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rematch
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rematch || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rematch/DESCRIPTION
/usr/lib64/R/library/rematch/INDEX
/usr/lib64/R/library/rematch/LICENSE
/usr/lib64/R/library/rematch/Meta/Rd.rds
/usr/lib64/R/library/rematch/Meta/features.rds
/usr/lib64/R/library/rematch/Meta/hsearch.rds
/usr/lib64/R/library/rematch/Meta/links.rds
/usr/lib64/R/library/rematch/Meta/nsInfo.rds
/usr/lib64/R/library/rematch/Meta/package.rds
/usr/lib64/R/library/rematch/NAMESPACE
/usr/lib64/R/library/rematch/NEWS.md
/usr/lib64/R/library/rematch/R/rematch
/usr/lib64/R/library/rematch/R/rematch.rdb
/usr/lib64/R/library/rematch/R/rematch.rdx
/usr/lib64/R/library/rematch/README.Rmd
/usr/lib64/R/library/rematch/README.md
/usr/lib64/R/library/rematch/help/AnIndex
/usr/lib64/R/library/rematch/help/aliases.rds
/usr/lib64/R/library/rematch/help/paths.rds
/usr/lib64/R/library/rematch/help/rematch.rdb
/usr/lib64/R/library/rematch/help/rematch.rdx
/usr/lib64/R/library/rematch/html/00Index.html
/usr/lib64/R/library/rematch/html/R.css
/usr/lib64/R/library/rematch/tests/testthat.R
/usr/lib64/R/library/rematch/tests/testthat/test.R
