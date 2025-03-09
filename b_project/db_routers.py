# class DatabaseRouter:
#     """A class to set routers for multiple dataabses for different apps."""


#     def db_for_read(self, model, **hints):
#         """Point database operations for specific apps to their respective databases."""
#         if model._meta.app_label == "blog":
#             return "default"
#         elif model._meta.app_label == "post":
#             return "mysql_db"
#         return "default"
    
#     def db_for_write(self, model, **hints):
#         """Point write operations to specific databases."""
#         if model._meta.app_label == "blog":
#             return "default"
#         elif model._meta.app_label == "post":
#             return "mysql_db"
#         return "default"
    
#     def allow_relation(self, obj1, obj2, **hints):
#         """Allow relations if both models are in the same database."""
#         db_set = {self.db_for_read(obj1), self.db_for_read(obj2)}
#         return len(db_set) == 1 or "default" in db_set


#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """Ensure apps' migrations only apply to their respective databases."""
#         if app_label == "blog":
#             return db == "default"
#         elif app_label == "post":
#             return db == "mysql_db"
#         return db == "default"
