from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_remove_doctor_city_remove_doctor_created_at_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                -- Ensure required column exists
                ALTER TABLE doctors_doctor
                ADD COLUMN IF NOT EXISTS bio TEXT;

                -- Remove legacy columns if they still exist
                ALTER TABLE doctors_doctor
                DROP COLUMN IF EXISTS office_address,
                DROP COLUMN IF EXISTS city,
                DROP COLUMN IF EXISTS department,
                DROP COLUMN IF EXISTS hospital_name,
                DROP COLUMN IF EXISTS license_number,
                DROP COLUMN IF EXISTS created_at;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
