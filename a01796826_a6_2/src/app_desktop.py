"""
Módulo de aplicación de escritorio para gestionar Customers, Hoteles y
Reservaciones. Utiliza Tkinter para la interfaz gráfica.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os

from .customer_service import CustomerService
from .hotel_service import HotelService
from .reservation_service import ReservationService


class HotelManagementApp:
    """
    Aplicación de escritorio para gestionar clientes, hoteles y reservaciones.
    """

    def __init__(self, root: tk.Tk):
        """
        Inicializa la aplicación.
        """
        self.root = root
        self.root.title("Sistema de Gestión de Hoteles")
        self.root.geometry("900x650")

        # Obtener ruta de datos
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(os.path.dirname(script_dir), "data")
        bd_path = os.path.join(data_dir, "bd.json")

        # Inicializar servicios
        self.customer_service = CustomerService(bd_path)
        self.hotel_service = HotelService(bd_path)
        self.reservation_service = ReservationService(bd_path)

        self.widgets = {
            "customers": {},
            "hotels": {},
            "reservations": {},
        }

        # Crear interfaz
        self._crear_interfaz()

    def run(self) -> None:
        """
        Inicia el bucle principal de la aplicación.
        """
        self.root.mainloop()

    def close(self) -> None:
        """
        Cierra la ventana principal.
        """
        self.root.destroy()

    def _crear_interfaz(self) -> None:
        """
        Crea la interfaz principal con pestañas.
        """
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Título
        titulo = ttk.Label(
            main_frame,
            text="Sistema de Gestión de Hoteles",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        # Notebook (pestañas)
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Crear pestañas
        tab_customers = ttk.Frame(notebook)
        tab_hotels = ttk.Frame(notebook)
        tab_reservations = ttk.Frame(notebook)

        notebook.add(tab_customers, text="Clientes")
        notebook.add(tab_hotels, text="Hoteles")
        notebook.add(tab_reservations, text="Reservaciones")

        # Llenar pestañas
        self._crear_tab_customers(tab_customers)
        self._crear_tab_hotels(tab_hotels)
        self._crear_tab_reservations(tab_reservations)

    def _crear_tab_customers(self, tab: ttk.Frame) -> None:
        """
        Crea la pestaña de clientes.
        """
        frame = ttk.Frame(tab, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        frame.rowconfigure(8, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        widgets = self.widgets["customers"]

        # === SECCIÓN CREAR ===
        ttk.Label(frame, text="CREAR NUEVO CLIENTE", font=("Arial", 11, "bold")).grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        ttk.Label(frame, text="Nombre:", font=("Arial", 10)).grid(
            row=1, column=0, sticky=tk.W, pady=5)
        widgets["entry_nombre"] = ttk.Entry(frame, width=30)
        widgets["entry_nombre"].grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(frame, text="Email:", font=("Arial", 10)).grid(
            row=2, column=0, sticky=tk.W, pady=5)
        widgets["entry_email"] = ttk.Entry(frame, width=30)
        widgets["entry_email"].grid(row=2, column=1, pady=5, padx=5)

        button_frame_crear = ttk.Frame(frame)
        button_frame_crear.grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(button_frame_crear, text="Crear Cliente", command=self._crear_customer).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame_crear, text="Limpiar", command=self._limpiar_customers).pack(
            side=tk.LEFT, padx=5)

        # === SECCIÓN BUSCAR/MODIFICAR/ELIMINAR ===
        ttk.Separator(frame, orient=tk.HORIZONTAL).grid(
            row=4, column=0, columnspan=2, sticky="ew", pady=15)
        ttk.Label(frame, text="BUSCAR / MODIFICAR / ELIMINAR", font=("Arial", 11, "bold")).grid(
            row=5, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        ttk.Label(frame, text="ID Cliente:", font=("Arial", 10)).grid(
            row=6, column=0, sticky=tk.W, pady=5)
        widgets["entry_id"] = ttk.Entry(frame, width=30)
        widgets["entry_id"].grid(row=6, column=1, pady=5, padx=5)

        ttk.Label(frame, text="Nuevo Nombre (opcional):", font=("Arial", 10)).grid(
            row=7, column=0, sticky=tk.W, pady=5)
        widgets["entry_nombre_mod"] = ttk.Entry(frame, width=30)
        widgets["entry_nombre_mod"].grid(row=7, column=1, pady=5, padx=5)

        ttk.Label(frame, text="Nuevo Email (opcional):", font=("Arial", 10)).grid(
            row=8, column=0, sticky=tk.W, pady=5)
        widgets["entry_email_mod"] = ttk.Entry(frame, width=30)
        widgets["entry_email_mod"].grid(row=8, column=1, pady=5, padx=5)

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=9, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Buscar", command=self._buscar_customer).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Modificar", command=self._modificar_customer).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Eliminar", command=self._eliminar_customer).pack(
            side=tk.LEFT, padx=5)

        # Área de resultados
        ttk.Label(frame, text="Resultado:", font=("Arial", 10, "bold")).grid(
            row=10, column=0, columnspan=2, sticky=tk.W, pady=(15, 5))
        widgets["text_result"] = scrolledtext.ScrolledText(
            frame, width=70, height=10, state=tk.DISABLED)
        widgets["text_result"].grid(row=11, column=0, columnspan=2, sticky="nsew")

    def _crear_tab_hotels(self, tab: ttk.Frame) -> None:
        """
        Crea la pestaña de hoteles.
        """
        frame = ttk.Frame(tab, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        frame.rowconfigure(9, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        widgets = self.widgets["hotels"]

        # === SECCIÓN CREAR ===
        ttk.Label(frame, text="CREAR NUEVO HOTEL", font=("Arial", 11, "bold")).grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        ttk.Label(frame, text="Nombre:", font=("Arial", 10)).grid(
            row=1, column=0, sticky=tk.W, pady=5)
        widgets["entry_nombre"] = ttk.Entry(frame, width=30)
        widgets["entry_nombre"].grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(frame, text="Ciudad:", font=("Arial", 10)).grid(
            row=2, column=0, sticky=tk.W, pady=5)
        widgets["entry_ciudad"] = ttk.Entry(frame, width=30)
        widgets["entry_ciudad"].grid(row=2, column=1, pady=5, padx=5)

        ttk.Label(frame, text="Total Habitaciones:", font=("Arial", 10)).grid(
            row=3, column=0, sticky=tk.W, pady=5)
        widgets["entry_habitaciones"] = ttk.Entry(frame, width=30)
        widgets["entry_habitaciones"].grid(row=3, column=1, pady=5, padx=5)

        button_frame_crear = ttk.Frame(frame)
        button_frame_crear.grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(button_frame_crear, text="Crear Hotel", command=self._crear_hotel).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame_crear, text="Limpiar", command=self._limpiar_hotels).pack(
            side=tk.LEFT, padx=5)

        # === SECCIÓN BUSCAR/MODIFICAR/ELIMINAR ===
        ttk.Separator(frame, orient=tk.HORIZONTAL).grid(
            row=5, column=0, columnspan=2, sticky="ew", pady=15)
        ttk.Label(frame, text="BUSCAR / MODIFICAR / ELIMINAR", font=("Arial", 11, "bold")).grid(
            row=6, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        ttk.Label(frame, text="ID Hotel:", font=("Arial", 10)).grid(
            row=7, column=0, sticky=tk.W, pady=5)
        widgets["entry_id"] = ttk.Entry(frame, width=30)
        widgets["entry_id"].grid(row=7, column=1, pady=5, padx=5)

        ttk.Label(frame, text="Nuevo Nombre (opcional):", font=("Arial", 10)).grid(
            row=8, column=0, sticky=tk.W, pady=5)
        widgets["entry_nombre_mod"] = ttk.Entry(frame, width=30)
        widgets["entry_nombre_mod"].grid(row=8, column=1, pady=5, padx=5)

        ttk.Label(frame, text="Nueva Ciudad (opcional):", font=("Arial", 10)).grid(
            row=9, column=0, sticky=tk.W, pady=5)
        widgets["entry_ciudad_mod"] = ttk.Entry(frame, width=30)
        widgets["entry_ciudad_mod"].grid(row=9, column=1, pady=5, padx=5)

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=10, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Buscar", command=self._buscar_hotel).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Modificar", command=self._modificar_hotel).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Eliminar", command=self._eliminar_hotel).pack(
            side=tk.LEFT, padx=5)

        # Área de resultados
        ttk.Label(frame, text="Resultado:", font=("Arial", 10, "bold")).grid(
            row=11, column=0, columnspan=2, sticky=tk.W, pady=(15, 5))
        widgets["text_result"] = scrolledtext.ScrolledText(
            frame, width=70, height=10, state=tk.DISABLED)
        widgets["text_result"].grid(row=12, column=0, columnspan=2, sticky="nsew")

    def _crear_tab_reservations(self, tab: ttk.Frame) -> None:
        """
        Crea la pestaña de reservaciones.
        """
        frame = ttk.Frame(tab, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        frame.rowconfigure(8, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        widgets = self.widgets["reservations"]

        # === SECCIÓN CREAR ===
        ttk.Label(frame, text="CREAR NUEVA RESERVACIÓN", font=("Arial", 11, "bold")).grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        ttk.Label(frame, text="ID Cliente:", font=("Arial", 10)).grid(
            row=1, column=0, sticky=tk.W, pady=5)
        widgets["entry_customer_id"] = ttk.Entry(frame, width=30)
        widgets["entry_customer_id"].grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(frame, text="ID Hotel:", font=("Arial", 10)).grid(
            row=2, column=0, sticky=tk.W, pady=5)
        widgets["entry_hotel_id"] = ttk.Entry(frame, width=30)
        widgets["entry_hotel_id"].grid(row=2, column=1, pady=5, padx=5)

        button_frame_crear = ttk.Frame(frame)
        button_frame_crear.grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(
            button_frame_crear, text="Crear Reservación",
            command=self._crear_reservation).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame_crear, text="Limpiar", command=self._limpiar_reservations).pack(
            side=tk.LEFT, padx=5)

        # === SECCIÓN VER/CANCELAR ===
        ttk.Separator(frame, orient=tk.HORIZONTAL).grid(
            row=4, column=0, columnspan=2, sticky="ew", pady=15)
        ttk.Label(frame, text="VER / CANCELAR", font=("Arial", 11, "bold")).grid(
            row=5, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))

        ttk.Label(frame, text="ID Reservación:", font=("Arial", 10)).grid(
            row=6, column=0, sticky=tk.W, pady=5)
        widgets["entry_id"] = ttk.Entry(frame, width=30)
        widgets["entry_id"].grid(row=6, column=1, pady=5, padx=5)

        button_frame = ttk.Frame(frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Ver", command=self._buscar_reservation).pack(
            side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancelar", command=self._cancelar_reservation).pack(
            side=tk.LEFT, padx=5)

        # Área de resultados
        ttk.Label(frame, text="Resultado:", font=("Arial", 10, "bold")).grid(
            row=8, column=0, columnspan=2, sticky=tk.W, pady=(15, 5))
        widgets["text_result"] = scrolledtext.ScrolledText(
            frame, width=70, height=10, state=tk.DISABLED)
        widgets["text_result"].grid(row=9, column=0, columnspan=2, sticky="nsew")

    # ===== OPERACIONES CLIENTES =====
    def _crear_customer(self) -> None:
        """
        Crea un nuevo cliente.
        """
        widgets = self.widgets["customers"]
        nombre = widgets["entry_nombre"].get().strip()
        email = widgets["entry_email"].get().strip()

        if not nombre or not email:
            messagebox.showerror("Error", "Por favor complete nombre y email")
            return

        try:
            customer = self.customer_service.crear_customer(nombre, email)
            self._mostrar_resultado_customer(
                f"✓ Cliente creado exitosamente\n"
                f"ID: {customer.id_customer}\n"
                f"Nombre: {customer.nombre}\n"
                f"Email: {customer.email}\n"
                f"Activo: {customer.activo}"
            )
            self._limpiar_customers()
        except (ValueError, KeyError, TypeError) as e:
            messagebox.showerror("Error", f"Error al crear cliente: {str(e)}")

    def _buscar_customer(self) -> None:
        """
        Busca un cliente por ID.
        """
        widgets = self.widgets["customers"]
        customer_id = widgets["entry_id"].get().strip()

        if not customer_id:
            messagebox.showerror("Error", "Ingrese un ID de cliente")
            return

        try:
            customer = self.customer_service.mostrar_customer(customer_id)
            if customer:
                self._mostrar_resultado_customer(
                    f"ID: {customer.id_customer}\n"
                    f"Nombre: {customer.nombre}\n"
                    f"Email: {customer.email}\n"
                    f"Activo: {customer.activo}"
                )
            else:
                self._mostrar_resultado_customer("✗ Cliente no encontrado")
        except (ValueError, KeyError, TypeError) as e:
            messagebox.showerror("Error", f"Error al buscar cliente: {str(e)}")

    def _modificar_customer(self) -> None:
        """
        Modifica un cliente existente.
        """
        widgets = self.widgets["customers"]
        customer_id = widgets["entry_id"].get().strip()
        nombre = widgets["entry_nombre_mod"].get().strip()
        email = widgets["entry_email_mod"].get().strip()

        if not customer_id:
            messagebox.showerror("Error", "Ingrese un ID de cliente")
            return

        if not nombre and not email:
            messagebox.showerror("Error", "Ingrese al menos nombre o email para modificar")
            return

        try:
            success = self.customer_service.modificar_customer(
                customer_id,
                nombre if nombre else None,
                email if email else None
            )
            if success:
                self._mostrar_resultado_customer("✓ Cliente modificado exitosamente")
                self._limpiar_customers()
            else:
                self._mostrar_resultado_customer("✗ No se pudo modificar el cliente")
        except (ValueError, KeyError, TypeError) as e:
            messagebox.showerror("Error", f"Error al modificar cliente: {str(e)}")

    def _eliminar_customer(self) -> None:
        """
        Elimina un cliente (borrado lógico).
        """
        widgets = self.widgets["customers"]
        customer_id = widgets["entry_id"].get().strip()

        if not customer_id:
            messagebox.showerror("Error", "Ingrese un ID de cliente")
            return

        if messagebox.askyesno("Confirmar", "¿Desea eliminar este cliente?"):
            try:
                success = self.customer_service.eliminar_customer(customer_id)
                if success:
                    self._mostrar_resultado_customer("✓ Cliente eliminado exitosamente")
                    self._limpiar_customers()
                else:
                    self._mostrar_resultado_customer("✗ Cliente no encontrado")
            except (ValueError, KeyError, TypeError) as e:
                messagebox.showerror("Error", f"Error al eliminar cliente: {str(e)}")

    def _limpiar_customers(self) -> None:
        """
        Limpia los campos de clientes.
        """
        widgets = self.widgets["customers"]
        widgets["entry_nombre"].delete(0, tk.END)
        widgets["entry_email"].delete(0, tk.END)
        widgets["entry_id"].delete(0, tk.END)
        widgets["entry_nombre_mod"].delete(0, tk.END)
        widgets["entry_email_mod"].delete(0, tk.END)

    def _mostrar_resultado_customer(self, texto: str) -> None:
        """
        Muestra resultado en el área de texto de clientes.
        """
        widgets = self.widgets["customers"]
        widgets["text_result"].config(state=tk.NORMAL)
        widgets["text_result"].delete(1.0, tk.END)
        widgets["text_result"].insert(tk.END, texto)
        widgets["text_result"].config(state=tk.DISABLED)

    # ===== OPERACIONES HOTELES =====
    def _crear_hotel(self) -> None:
        """
        Crea un nuevo hotel.
        """
        widgets = self.widgets["hotels"]
        nombre = widgets["entry_nombre"].get().strip()
        ciudad = widgets["entry_ciudad"].get().strip()
        habitaciones = widgets["entry_habitaciones"].get().strip()

        if not nombre or not ciudad or not habitaciones:
            messagebox.showerror("Error", "Complete todos los campos")
            return

        try:
            habitaciones_int = int(habitaciones)
            if habitaciones_int <= 0:
                messagebox.showerror("Error", "Habitaciones debe ser un número positivo")
                return

            hotel = self.hotel_service.crear_hotel(nombre, ciudad, habitaciones_int)
            self._mostrar_resultado_hotel(
                f"✓ Hotel creado exitosamente\n"
                f"ID: {hotel.id_hotel}\n"
                f"Nombre: {hotel.nombre}\n"
                f"Ciudad: {hotel.ciudad}\n"
                f"Habitaciones: {hotel.total_habitaciones}\n"
                f"Activo: {hotel.activo}"
            )
            self._limpiar_hotels()
        except ValueError:
            messagebox.showerror("Error", "Habitaciones debe ser un número entero")
        except (KeyError, TypeError) as e:
            messagebox.showerror("Error", f"Error al crear hotel: {str(e)}")

    def _buscar_hotel(self) -> None:
        """
        Busca un hotel por ID.
        """
        widgets = self.widgets["hotels"]
        hotel_id = widgets["entry_id"].get().strip()

        if not hotel_id:
            messagebox.showerror("Error", "Ingrese un ID de hotel")
            return

        try:
            hotel = self.hotel_service.mostrar_hotel(hotel_id)
            if hotel:
                self._mostrar_resultado_hotel(
                    f"ID: {hotel.id_hotel}\n"
                    f"Nombre: {hotel.nombre}\n"
                    f"Ciudad: {hotel.ciudad}\n"
                    f"Habitaciones: {hotel.total_habitaciones}\n"
                    f"Activo: {hotel.activo}"
                )
            else:
                self._mostrar_resultado_hotel("✗ Hotel no encontrado")
        except (ValueError, KeyError, TypeError) as e:
            messagebox.showerror("Error", f"Error al buscar hotel: {str(e)}")

    def _modificar_hotel(self) -> None:
        """
        Modifica un hotel existente.
        """
        widgets = self.widgets["hotels"]
        hotel_id = widgets["entry_id"].get().strip()
        nombre = widgets["entry_nombre_mod"].get().strip()
        ciudad = widgets["entry_ciudad_mod"].get().strip()

        if not hotel_id:
            messagebox.showerror("Error", "Ingrese un ID de hotel")
            return

        if not nombre and not ciudad:
            messagebox.showerror("Error", "Ingrese al menos un campo para modificar")
            return

        try:
            success = self.hotel_service.modificar_hotel(
                hotel_id,
                nombre if nombre else None,
                ciudad if ciudad else None,
                None
            )
            if success:
                self._mostrar_resultado_hotel("✓ Hotel modificado exitosamente")
                self._limpiar_hotels()
            else:
                self._mostrar_resultado_hotel("✗ No se pudo modificar el hotel")
        except ValueError:
            messagebox.showerror("Error", "Habitaciones debe ser un número entero")
        except (KeyError, TypeError) as e:
            messagebox.showerror("Error", f"Error al modificar hotel: {str(e)}")

    def _eliminar_hotel(self) -> None:
        """
        Elimina un hotel (borrado lógico).
        """
        widgets = self.widgets["hotels"]
        hotel_id = widgets["entry_id"].get().strip()

        if not hotel_id:
            messagebox.showerror("Error", "Ingrese un ID de hotel")
            return

        if messagebox.askyesno("Confirmar", "¿Desea eliminar este hotel?"):
            try:
                success = self.hotel_service.eliminar_hotel(hotel_id)
                if success:
                    self._mostrar_resultado_hotel("✓ Hotel eliminado exitosamente")
                    self._limpiar_hotels()
                else:
                    self._mostrar_resultado_hotel("✗ Hotel no encontrado")
            except (ValueError, KeyError, TypeError) as e:
                messagebox.showerror("Error", f"Error al eliminar hotel: {str(e)}")

    def _limpiar_hotels(self) -> None:
        """
        Limpia los campos de hoteles.
        """
        widgets = self.widgets["hotels"]
        widgets["entry_nombre"].delete(0, tk.END)
        widgets["entry_ciudad"].delete(0, tk.END)
        widgets["entry_habitaciones"].delete(0, tk.END)
        widgets["entry_id"].delete(0, tk.END)
        widgets["entry_nombre_mod"].delete(0, tk.END)
        widgets["entry_ciudad_mod"].delete(0, tk.END)

    def _mostrar_resultado_hotel(self, texto: str) -> None:
        """
        Muestra resultado en el área de texto de hoteles.
        """
        widgets = self.widgets["hotels"]
        widgets["text_result"].config(state=tk.NORMAL)
        widgets["text_result"].delete(1.0, tk.END)
        widgets["text_result"].insert(tk.END, texto)
        widgets["text_result"].config(state=tk.DISABLED)

    # ===== OPERACIONES RESERVACIONES =====
    def _crear_reservation(self) -> None:
        """
        Crea una nueva reservación.
        """
        widgets = self.widgets["reservations"]
        customer_id = widgets["entry_customer_id"].get().strip()
        hotel_id = widgets["entry_hotel_id"].get().strip()

        if not customer_id or not hotel_id:
            messagebox.showerror("Error", "Ingrese ID de cliente e hotel")
            return

        try:
            reservation = self.reservation_service.crear_reservation(customer_id, hotel_id)
            if reservation:
                self._mostrar_resultado_reservation(
                    f"✓ Reservación creada exitosamente\n"
                    f"ID: {reservation.id_reservation}\n"
                    f"Cliente ID: {reservation.id_customer}\n"
                    f"Hotel ID: {reservation.id_hotel}\n"
                    f"Activa: {reservation.activo}"
                )
                self._limpiar_reservations()
            else:
                self._mostrar_resultado_reservation("✗ No se pudo crear la reservación")
        except (ValueError, KeyError, TypeError) as e:
            messagebox.showerror("Error", f"Error al crear reservación: {str(e)}")

    def _buscar_reservation(self) -> None:
        """
        Busca una reservación por ID.
        """
        widgets = self.widgets["reservations"]
        reservation_id = widgets["entry_id"].get().strip()

        if not reservation_id:
            messagebox.showerror("Error", "Ingrese un ID de reservación")
            return

        try:
            reservation = self.reservation_service.mostrar_reservation(reservation_id)
            if reservation:
                customer = self.customer_service.mostrar_customer(reservation.id_customer)
                hotel = self.hotel_service.mostrar_hotel(reservation.id_hotel)

                resultado = f"ID: {reservation.id_reservation}\n"
                resultado += f"Cliente: {customer.nombre if customer else 'No encontrado'}\n"
                resultado += f"Hotel: {hotel.nombre if hotel else 'No encontrado'}\n"
                resultado += f"Activa: {reservation.activo}"

                self._mostrar_resultado_reservation(resultado)
            else:
                self._mostrar_resultado_reservation("✗ Reservación no encontrada")
        except (ValueError, KeyError, TypeError) as e:
            messagebox.showerror("Error", f"Error al buscar reservación: {str(e)}")

    def _cancelar_reservation(self) -> None:
        """
        Cancela una reservación.
        """
        widgets = self.widgets["reservations"]
        reservation_id = widgets["entry_id"].get().strip()

        if not reservation_id:
            messagebox.showerror("Error", "Ingrese un ID de reservación")
            return

        if messagebox.askyesno("Confirmar", "¿Desea cancelar esta reservación?"):
            try:
                success = self.reservation_service.cancelar_reservation(reservation_id)
                if success:
                    self._mostrar_resultado_reservation("✓ Reservación cancelada exitosamente")
                    self._limpiar_reservations()
                else:
                    self._mostrar_resultado_reservation("✗ Reservación no encontrada")
            except (ValueError, KeyError, TypeError) as e:
                messagebox.showerror("Error", f"Error al cancelar: {str(e)}")

    def _limpiar_reservations(self) -> None:
        """
        Limpia los campos de reservaciones.
        """
        widgets = self.widgets["reservations"]
        widgets["entry_customer_id"].delete(0, tk.END)
        widgets["entry_hotel_id"].delete(0, tk.END)
        widgets["entry_id"].delete(0, tk.END)

    def _mostrar_resultado_reservation(self, texto: str) -> None:
        """
        Muestra resultado en el área de texto de reservaciones.
        """
        widgets = self.widgets["reservations"]
        widgets["text_result"].config(state=tk.NORMAL)
        widgets["text_result"].delete(1.0, tk.END)
        widgets["text_result"].insert(tk.END, texto)
        widgets["text_result"].config(state=tk.DISABLED)


def main() -> None:
    """
    Función principal que inicia la aplicación.
    """
    root = tk.Tk()
    app = HotelManagementApp(root)
    app.run()


if __name__ == "__main__":
    main()
