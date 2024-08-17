import sqlite3
            parameter_date = input("Enter parameter date (YYYY-MM-DD): ")
            insert_health_parameters(patient_id, heart_rate, systolic, diastolic, body_temperature, oxygen_saturation, parameter_date)
        elif choice == '7':
            record_id = int(input("Enter the record ID to update: "))
            heart_rate = int(input("Enter heart rate (bpm): "))
            systolic = int(input("Enter systolic blood pressure (mmHg): "))
            diastolic = int(input("Enter diastolic blood pressure (mmHg): "))
            body_temperature = float(input("Enter body temperature (°C): "))
            oxygen_saturation = float(input("Enter oxygen saturation (%): "))
            update_health_parameters(record_id, heart_rate, systolic, diastolic, body_temperature, oxygen_saturation)
        elif choice == '8':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

conn.close()
