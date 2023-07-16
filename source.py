class Property:
    def __set_name__(self, owner, name):
        class_name = str(owner).split("'")[1].split(".")[-1]
        if class_name not in ["CPU", "SSD", "HDD"]:
            self.name = '_' + name
        else: 
            self.name = name
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Resource:
    NAME = str
    MANUFACTURER = str
    TOTAL = int
    ALLOCATED = int

    name = Property()
    manufacturer = Property()
    @classmethod
    def verify_member_Resource(cls, name, manufacturer, total, allocated):
        return isinstance(name, cls.NAME) and \
               isinstance(manufacturer, cls.MANUFACTURER) and \
               isinstance(total, cls.TOTAL) and \
               isinstance(allocated, cls.ALLOCATED)
    def __init__(self, name, manufacturer, total, allocated):
        if self.verify_member_Resource(name, manufacturer, total, allocated):
            self.name = name #tvyal apranqi anvanumy
            self.manufacturer = manufacturer # artadrox kazmakerputyuny
            self.__total = total #yndhanur apranqneri qanaky
            self.__allocated = allocated #ayn qanaky vory vajarvel e
        else:
            raise TypeError("The types you provided do not match what was requested")
    
    def __str__(self):
        return self.name
    def __repr__(self): 
        return f"{self.__class__.__name__}(name={self._name}, manufacturer={self._manufacturer}, total={self.__total}, allocated={self.__allocated}"
    def claim(self, n):#(tramadrel) ardyoq karox e tramadrvel n qanakov apranqner
        if n <= self.__total - self.__allocated:
            self.__allocated += n
            print(f"Claimed {n} {self._name}")
        else:
            print("Insufficient inventory available.")
    def freeup(self, n):#(veradardznel) ardyoq hnaravor e n apranq ver.
        if n <= self.__allocated:
            self.__allocated -= n
            print(f"Freed up {n} {self._name}")
        else:
            print("Invalid number to free up.")
    def died(self, n):#(veradardzvox) ev yndhanrapes veracvox apranqner
        if n <= self.__allocated:
            self.__allocated -= n
            self.__total -= n
            print(f"Removed {n} {self._name} form inventory")
        else:
            print("Invalid number to remove from inventory.")
    def purchased(self, n):#avelacnum en nor apranqner
        self.__total += n
        print(f"Purchased {n} {self._name}")
    @property
    def allocated(self):
        return self.__allocated
    @property
    def total(self):
        return self.__total
    @property
    def category(self):#veradardznum e tvayl class-i anuny poqratarerov
        return self.__class__.__name__.lower()

class Storage(Resource):
    CAPACITY = int

    capacity_GB = Property()

    @classmethod
    def verify_member_Storage(cls, capacity_GB):
        return isinstance(capacity_GB, cls.CAPACITY)
    
    def __init__(self, name, manufacturer, total, allocated, capacity_GB):
        super().__init__(name, manufacturer, total, allocated)
        if self.verify_member_Storage(capacity_GB):
            self.capacity_GB = capacity_GB
        else:
            raise TypeError("The types you provided do not match what was requested")
    
    def __repr__(self):
        return super().__repr__() + f", capacity_GB={self._capacity_GB}"

class CPU(Storage):
    CORES = int
    INTERFACE = str
    SOCKET = str
    POWER_WATTS = int

    cores = Property()
    interface = Property()
    socket = Property()
    power_watts = Property()
    
    @classmethod
    def verify_member_CPU(cls, cores, interface, socket, power_watts):
        return isinstance(cores, cls.CORES) and \
               isinstance(interface, cls.interface) and \
               isinstance(socket, cls.SOCKET) and \
               isinstance(power_watts, cls.POWER_WATTS)
    
    def __init__(self, name, manufacturer, total, allocated, capacity_GB, cores, interface, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        if self.verify_member_CPU(cores, interface, socket, power_watts):
            self.cores = cores
            self.interface = interface
            self.socket = socket
            self.power_watts = power_watts
        else:
            raise TypeError("The types you provided do not match what was requested")

    def __repr__(self):
        return super().__repr__() + f", cores={self.cores}, interface={self.interface}, socket={self.socket}, power_watts={self.power_watts}"

class HDD(Storage):
    SIZE = int
    RPM = int

    size = Property()
    rpm = Property()

    @classmethod
    def verify_member_HDD(cls, size, rpm):
        return isinstance(size, cls.SIZE) and \
               isinstance(rpm, cls.RPM)

    def __init__(self, name, manufacturer, total, allocated, capacity_GB, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        if self.verify_member_HDD(size, rpm):
            self.size = size
            self.rpm = rpm
        else:
            raise TypeError("The types you provided do not match what was requested")
    
    def __repr__(self):
        return super().__repr__() + f", size={self.size}, rpm={self.rpm})"

class SSD(Storage):
    INTERFACE = str

    interface = Property()

    @classmethod
    def verify_member_SSD(cls, interface):
        return isinstance(interface, cls.INTERFACE)

    def __init__(self, name, manufacturer, total, allocated, capacity_GB, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        if self.verify_member_SSD(interface):
            self.interface = interface
        else:
            raise TypeError("The types you provided do not match what was requested")

    def __repr__(self):
        return super().__repr__() + f", interface={self.interface})"




