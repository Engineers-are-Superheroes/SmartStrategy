cd backend
export DJANGO_ENV=production
waitress-serve SmartStrategy.wsgi:application
cd ..